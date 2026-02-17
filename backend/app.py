from flask import Flask, request
from flask_cors import CORS
import pdfplumber, io, base64, os, math, requests, uuid
import pytesseract
from PIL import Image

from db import (
    init_db, insert_chunk, get_chunks,
    create_session, get_session,
    add_message, get_history
)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = Flask(__name__)
CORS(app)

app.config["MAX_CONTENT_LENGTH"] = 500 * 1024 * 1024
os.makedirs("storage", exist_ok=True)

MAX_CHUNKS_PER_PDF = 3500


# =========================
# RAG HELPERS
# =========================
def chunk_text(text, size=650, overlap=120):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        c = " ".join(words[i:i+size])
        if len(c.strip()) > 80:
            chunks.append(c)
        i += size - overlap
    return chunks


def cosine(a, b):
    if not a or not b:
        return 0.0

    # ensure same length
    n = min(len(a), len(b))
    if n == 0:
        return 0.0

    dot = 0.0
    ma = 0.0
    mb = 0.0

    for i in range(n):
        x = a[i]
        y = b[i]
        dot += x * y
        ma += x * x
        mb += y * y

    if ma == 0 or mb == 0:
        return 0.0

    return dot / (math.sqrt(ma) * math.sqrt(mb))


def ollama_embed(text):
    try:
        r = requests.post(
            "http://localhost:11434/api/embeddings",
            json={"model": "nomic-embed-text", "prompt": text},
            timeout=60
        )
        return r.json().get("embedding", [])
    except:
        return []


def generate(prompt):
    try:
        r = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "llama3", "prompt": prompt, "stream": False},
            timeout=120
        )
        return r.json().get("response", "")
    except:
        return "Answer is not present in the PDF."


# =========================
# ROUTES
# =========================
@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/new-chat", methods=["POST"])
def new_chat():
    pdf_id = request.json.get("pdf_id")
    sid = str(uuid.uuid4())
    create_session(sid, pdf_id)
    return {"session_id": sid}


@app.route("/history", methods=["POST"])
def history():
    sid = request.json.get("session_id")
    return get_history(sid)


@app.route("/process-pdf", methods=["POST"])
def process_pdf():
    raw = request.json.get("pdf_data")
    pdf_id = request.json.get("pdf_id")

    if not raw or not pdf_id:
        return {"error": "pdf_data & pdf_id required"}, 400

    pdf_bytes = base64.b64decode(raw)
    cid = 0

    try:
        with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:

            for pno, page in enumerate(pdf.pages, 1):

                text = page.extract_text() or ""

                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        text += "\n" + " | ".join([str(c) if c else "" for c in row])

                if len(text.strip()) < 40:
                    img = page.to_image(resolution=300).original
                    text = pytesseract.image_to_string(img)

                for c in chunk_text(text):

                    emb = ollama_embed(c)
                    if not emb:
                        continue
                    if len(c.split()) < 60:
                        continue

                    insert_chunk(pdf_id, pno, c, emb)
                    cid += 1

                    if cid > MAX_CHUNKS_PER_PDF:
                        break

    except Exception as e:
        print("PDF error:", e)
        return {"error": "failed to read pdf"}, 500

    return {"success": True, "chunks": cid}


@app.route("/query", methods=["POST"])
@app.route("/query", methods=["POST"])
def query():

    # ---------- get inputs ----------
    data = request.json or {}
    q = data.get("question", "").strip()
    sid = data.get("session_id")

    if not q:
        return {"answer": "Please ask a question."}

    # ---------- detect query type ----------
    q_lower = q.lower()

    if "summary" in q_lower or "summarize" in q_lower:
        mode = "summary"
    elif "notes" in q_lower:
        mode = "notes"
    else:
        mode = "qa"

    # ---------- session check ----------
    pdf_id = get_session(sid)
    if not pdf_id:
        return {"answer": "Invalid session."}

    # ---------- embed question ----------
    qemb = ollama_embed(q)
    if not qemb:
        return {"answer": "Embedding failed."}

    # ---------- load chunks ----------
    rows = get_chunks(pdf_id)
    if not rows:
        return {"answer": "PDF not processed yet."}

    import json

    # ---------- compute similarity ----------
    scored = []

    for page, text, emb in rows:
        try:
            emb_vec = json.loads(emb)
        except:
            continue

        score = cosine(qemb, emb_vec)

        # QA mode → filter weak chunks
        if mode == "qa":
            if score > 0.20:
                scored.append((score, text, page))
        else:
            # summary/notes → keep all chunks
            scored.append((score, text, page))

    if not scored:
        return {"answer": "Answer is not present in the PDF."}

    scored.sort(key=lambda x: x[0], reverse=True)

    # ---------- select chunks ----------
    top_chunks = []

    if mode in ["summary", "notes"]:

        # take representative chunks across pages
        page_map = {}

        for score, text, page in scored:
            if page not in page_map:
                page_map[page] = text

            if len(page_map) >= 8:
                break

        # fallback if similarity failed completely
        if not page_map:
            for row in rows[:8]:
                page_map[row[0]] = row[1]

        top_chunks = list(page_map.values())

    else:
        # QA mode → strong chunks only
        for score, text, page in scored:
            if score > 0.30:
                top_chunks.append(text)

            if len(top_chunks) >= 4:
                break

    if not top_chunks:
        return {"answer": "Answer is not present in the PDF."}

    ctx = "\n\n".join(top_chunks)

    # ---------- instruction ----------
    if mode == "summary":
        instruction = "Provide a concise summary of the document."
    elif mode == "notes":
        instruction = "Create structured bullet-point notes from the document."
    else:
        instruction = "Answer the question using only the context."

    # ---------- prompt ----------
    prompt = f"""
You are ChatPDF AI.

{instruction}

Rules:
1. Use ONLY the context.
2. If answer not present, say exactly:
   "Answer is not present in the PDF."
3. Do not invent information.

Context:
{ctx}

Question:
{q}

Answer:
"""

    ans = generate(prompt)

    # ---------- save chat ----------
    add_message(sid, "user", q)
    add_message(sid, "ai", ans)

    return {"answer": ans}



if __name__ == "__main__":
    init_db()
    app.run(port=5000, debug=True)
