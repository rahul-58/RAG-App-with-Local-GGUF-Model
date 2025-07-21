# 📄 RAG PDF QA App with Local GGUF Model

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to upload one or more PDF files, ask questions, and receive AI-generated answers using a **local LLM in `.gguf` format** (via `llama.cpp`). It runs entirely offline and uses fast local embeddings and a vector store.

## 🚀 Features

- Upload and parse multiple PDF files
- Split documents into overlapping chunks for context retention
- Embed and index using `MiniLM` + FAISS
- Query documents with natural language questions
- Generate answers using a local LLM (`.gguf`) with `llama-cpp-python`
- Fully private & local — no external APIs required

## 🧠 How It Works

1. PDFs → Text → Chunks
2. Chunks → Embeddings → FAISS index
3. Question → Embedding → Similarity Search
4. Top chunks + question → Prompt to LLM
5. Local `.gguf` model generates answer

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **Embedding**: Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Vector Store**: FAISS
- **LLM Inference**: `llama.cpp` via `llama-cpp-python`
- **PDF Parsing**: PyMuPDF

## 📁 Folder Structure

rag_gguf_pdf_qa/
├── app.py # Streamlit frontend
├── rag_engine.py # RAG logic (embedding, retrieval, LLM)
├── utils.py # PDF parsing and text chunking
├── models/
│ └── your-model.gguf # Downloaded LLM (e.g., Mistral, Zephyr)
└── requirements.txt # Python dependencies


## 🔧 Setup Instructions

1. **Clone the repo**

git clone https://github.com/your-username/rag-gguf-pdf-qa.git
cd rag-gguf-pdf-qa

2. **Set up virtual environment**
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate

3. **Install dependencies**
pip install -r requirements.txt

4. **Download a GGUF model**
Choose from TheBloke models on Hugging Face, e.g.:

Mistral-7B-Instruct-v0.2.Q4_K_M.gguf

zephyr-7B-beta.Q4_K_M.gguf

Place it in the models/ folder.

5. **Run the app**
streamlit run app.py