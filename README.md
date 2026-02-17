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
