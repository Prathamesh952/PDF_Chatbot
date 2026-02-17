# PDF_Chatbot
RAG-based PDF assistant that lets users upload documents, generate embeddings, and ask semantic questions. Returns accurate Markdown answers, summaries, notes, and auto-generated questions using vector search and LLMs.

<h1 align="center">📄 PDF.QA AI – Intelligent Document Assistant</h1>

<p align="center">
An AI-powered document assistant that allows users to upload PDFs and interact with them using natural language queries.
</p>

<hr>

<h2>🚀 Project Overview</h2>

<p>
PDF.QA AI is a lightweight AI-based document interaction system designed for academic demonstration and practical use. 
Users can upload PDF files and ask questions related to the document content. The backend extracts text from the PDF, processes it, 
and generates context-aware responses using an AI model.
</p>

<p>
Unlike simple keyword search tools, this system retrieves relevant context from the uploaded document and generates structured answers. 
It also includes a safeguard to avoid generating responses when the answer is not present in the document.
</p>

<hr>

<h2>✨ Features</h2>

<ul>
<li>📄 Upload and process PDF documents</li>
<li>🔍 Context-based document retrieval</li>
<li>🤖 AI-powered Question Answering</li>
<li>📝 Basic notes and summary generation</li>
<li>📌 Structured response formatting</li>
<li>💾 Local chat history storage</li>
<li>🛡 Prevents answers when information is unavailable</li>
</ul>

<hr>

<h2>🧠 System Architecture</h2>

<p>The system follows a simplified document assistant pipeline:</p>

<pre>
User Uploads PDF
        ↓
Backend receives file
        ↓
Text Extraction & Processing
        ↓
Document stored locally
        ↓
User asks question
        ↓
Relevant context retrieved
        ↓
AI generates response
        ↓
Frontend displays answer
</pre>

<hr>

<h2>🏗 Architecture Diagram</h2>

<pre>
 ┌──────────────┐
 │    Client    │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │   Frontend   │
 │ HTML/CSS/JS  │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Python Backend│
 │    app.py     │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ PDF Parsing  │
 │ Text Process │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ Local Storage│
 │ JSON files   │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │ AI Generator │
 └──────┬───────┘
        ↓
 ┌──────────────┐
 │  Response UI │
 └──────────────┘
</pre>

<hr>

<h2>⚙️ Tech Stack</h2>

<ul>
<li><b>Backend:</b> Python (single server file - app.py)</li>
<li><b>PDF Processing:</b> Python PDF libraries</li>
<li><b>Storage:</b> JSON files (lightweight local storage)</li>
<li><b>Frontend:</b> HTML, CSS, JavaScript</li>
<li><b>AI Integration:</b> LLM-based response generation</li>
</ul>

<hr>

<h2>🎯 Use Cases</h2>

<ul>
<li>📚 Student study assistant</li>
<li>📑 Research paper exploration</li>
<li>🧾 Document search demo system</li>
<li>📖 Academic AI project</li>
</ul>

<hr>

<h2>📂 Project File Structure</h2>

<pre>
chatpdf-ai/
│
├── backend/
│   ├── app.py                   # Main backend server (upload, processing, QA)
│   ├── requirements.txt         # Backend dependencies
│   │
│   └── storage/
│       ├── documents.json       # Stores processed document data
│       └── chat_history.json    # Stores previous user interactions
│
├── frontend/
│   ├── index.html               # Main UI
│   ├── style.css                # Styling
│   ├── app.js                   # Handles API calls
│   └── logo.png                 # UI asset
│
└── README.md
</pre>

<hr>

<h2>🧠 Architecture Explanation</h2>

<ul>
<li><b>Backend (app.py):</b> Handles PDF upload, parsing, processing, and AI-based question answering.</li>
<li><b>Storage Layer:</b> JSON files store processed documents and chat history locally, acting as a lightweight database.</li>
<li><b>Frontend:</b> Provides a simple interface to upload PDFs, ask questions, and view answers.</li>
<li><b>Communication Flow:</b> Frontend sends requests → backend processes document → AI generates response → frontend displays result.</li>
</ul>

<hr>

<h2>📌 Future Improvements</h2>

<ul>
<li>Database integration instead of JSON storage</li>
<li>Multi-PDF support</li>
<li>Improved semantic retrieval</li>
<li>Page citation highlighting</li>
<li>Streaming responses</li>
<li>Cloud deployment</li>
</ul>

<hr>

<p align="center">
Built as an academic AI project demonstrating document intelligence workflow and AI-assisted document interaction.
</p>
