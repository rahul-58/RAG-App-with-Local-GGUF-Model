# 📄 RAG PDF QA App with Local GGUF Model

This project is a **Retrieval-Augmented Generation (RAG)** application that allows users to upload one or more PDF files, ask questions, and receive **AI-generated  context-aware answers** using a **local LLM in `.gguf` format** (via `llama.cpp`). Built with **Streamlit**, it provides an interactive web UI with complete privacy — **no external APIs or cloud LLMs used**.

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

```
rag_gguf_pdf_qa/
├── app.py                      # Streamlit frontend
├── rag_engine.py               # RAG logic (embedding, retrieval, LLM)
├── utils.py                    # PDF parsing and text chunking
├── models/
│ └── your-model.gguf           # Downloaded LLM (e.g., Mistral, Zephyr)
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md
```


## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/rahul-58/RAG-App-with-Local-GGUF-Model.git
cd RAG-App-with-Local-GGUF-Model
```

2. **Set up virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Download a GGUF model**

```
Choose any model on Hugging Face, e.g.:

Mistral-7B-Instruct-v0.2.Q4_K_M.gguf

zephyr-7B-beta.Q4_K_M.gguf

Place it in the models/ folder.
```

5. **Run the app**

```bash
streamlit run app.py
```

Open [http://localhost:8501] in your browser.

---

## 📌 Example Use Case

1. Upload your course notes or technical research papers as PDFs  
2. Ask: *"What are the main contributions of this paper?"* or *"Explain the algorithm used in section 3."*  
3. The app retrieves the most relevant chunks and generates an answer using the local model

---
