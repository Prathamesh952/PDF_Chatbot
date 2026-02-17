# PDF_Chatbot
RAG-based PDF assistant that lets users upload documents, generate embeddings, and ask semantic questions. Returns accurate Markdown answers, summaries, notes, and auto-generated questions using vector search and LLMs.

<h1 align="center">📄 PDF.QA AI – Intelligent Document Assistant</h1>

<p align="center">
An AI-powered document assistant that enables semantic question answering, summarization, and note generation from PDFs using Retrieval-Augmented Generation (RAG).
</p>

<hr>

<h2>🚀 Project Overview</h2>

<p>
PDF.QA AI is an intelligent document processing system that allows users to upload PDFs and interact with them using natural language queries.  
The system converts documents into embeddings, stores them in a vector database, retrieves relevant context, and generates structured answers using an LLM.
</p>

<p>
Unlike traditional keyword search, this system performs <b>semantic retrieval</b>, ensuring higher accuracy and context-aware responses.  
It also includes hallucination control to prevent answers when the information is not present in the document.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
<li>📄 Upload and process PDF documents</li>
<li>🔍 Semantic search using vector embeddings</li>
<li>🤖 AI-powered Question Answering</li>
<li>📝 Automatic Notes Generation</li>
<li>📚 Smart PDF Summarization</li>
<li>❓ Auto-generated questions from document</li>
<li>📌 Markdown formatted responses</li>
<li>🛡 Hallucination control (no fake answers)</li>
</ul>

<hr>

<h2>🧠 System Architecture</h2>

<p>The system follows a production-style Retrieval-Augmented Generation pipeline:</p>

<pre>
User Uploads PDF
        ↓
Document Processing Pipeline
(Text Extraction + OCR + Cleaning)
        ↓
Chunking & Metadata Creation
        ↓
Embedding Model
        ↓
Vector Database Storage
        ↓
User Question
        ↓
Semantic Retriever
        ↓
LLM Generator
        ↓
Markdown Formatted Answer
</pre>

<hr>

<h2>🏗 Architecture Diagram</h2>

<pre>
 ┌──────────────┐
 │    Client    │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │  FastAPI API │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ PDF Ingestion│
 │ Parsing/OCR  │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Chunking     │
 │ + Metadata   │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Embeddings   │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Vector DB    │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Retriever    │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │   LLM (RAG)  │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Markdown Ans │
 └──────────────┘
</pre>

<hr>

<h2>⚙️ Tech Stack</h2>

<ul>
<li><b>Backend:</b> FastAPI, Python</li>
<li><b>Vector Database:</b> ChromaDB</li>
<li><b>Embeddings:</b> OpenAI / Sentence Transformers</li>
<li><b>LLM:</b> OpenAI / Local LLM (Ollama)</li>
<li><b>PDF Parsing:</b> PyMuPDF, OCR support</li>
<li><b>Frontend:</b> HTML, CSS, JS</li>
</ul>

<hr>

<h2>🎯 Use Cases</h2>

<ul>
<li>📚 Student study assistant</li>
<li>📑 Research paper exploration</li>
<li>🏢 Enterprise document search</li>
<li>📖 Knowledge base assistant</li>
</ul>

<hr>

<h2>📌 Future Improvements</h2>

<ul>
<li>Multi-PDF chat support</li>
<li>Page-level citation highlighting</li>
<li>Streaming responses</li>
<li>Role-based document access</li>
<li>Cloud deployment with scalable vector storage</li>
</ul>

<hr>

<p align="center">
Built as a production-style RAG system demonstrating modern AI document intelligence architecture.
</p>


<hr>

<h2>▶️ How to Run This Project (Step-by-Step)</h2>

<p>
To keep the repository lightweight, the <b>virtual environment (venv)</b> folder has been removed due to GitHub file size limits.  
Please create your own virtual environment before running the project.
</p>

<h3>1️⃣ Clone the Repository</h3>

<pre>
git clone https://github.com/your-username/pdf-qa-ai.git
cd pdf-qa-ai
</pre>

<h3>2️⃣ Create Virtual Environment</h3>

<pre>
python -m venv venv
</pre>

<h3>3️⃣ Activate Virtual Environment</h3>

<p><b>Windows:</b></p>
<pre>
venv\Scripts\activate
</pre>

<p><b>Mac/Linux:</b></p>
<pre>
source venv/bin/activate
</pre>

<h3>4️⃣ Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>5️⃣ Add Environment Variables</h3>

<p>Create a <b>.env</b> file in the project root and add:</p>

<pre>
OPENAI_API_KEY=your_api_key_here
</pre>

<p>If running with local models, this step can be skipped.</p>

<h3>6️⃣ Start Backend Server</h3>

<pre>
uvicorn app.main:app --reload
</pre>

<p>The API will start at:</p>

<pre>
http://127.0.0.1:8000
</pre>

<p>Interactive API docs available at:</p>

<pre>
http://127.0.0.1:8000/docs
</pre>

<h3>7️⃣ Run Frontend</h3>

<p>Open the frontend file directly in browser:</p>

<pre>
frontend/index.html
</pre>

<h3>8️⃣ Test the System</h3>

<ul>
<li>Upload a PDF</li>
<li>Ask a question</li>
<li>The AI will return a Markdown-formatted answer</li>
</ul>

<hr>

<h2>⚠️ Important Notes</h2>

<ul>
<li>The <b>venv folder is intentionally excluded</b> to keep the repo small.</li>
<li>If the project does not run, reinstall dependencies.</li>
<li>Ensure Python version is 3.10 – 3.12.</li>
<li>For best accuracy, use text-based PDFs instead of scanned ones.</li>
</ul>
