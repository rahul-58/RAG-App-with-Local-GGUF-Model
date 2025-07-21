import streamlit as st
from utils import extract_text_from_pdf, chunk_text
from rag_engine import RAGPipeline

st.set_page_config(page_title="PDF QA RAG App", layout="wide")
st.title("RAG App with Local GGUF Model")

model_path = "models/dolphin-2.6-mistral-7b.Q4_K_M.gguf"
rag = RAGPipeline(model_path)

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    all_text = ""
    for file in uploaded_files:
        st.info(f"Parsing {file.name}...")
        all_text += extract_text_from_pdf(file)

    chunks = chunk_text(all_text)
    st.success(f"Split into {len(chunks)} chunks.")
    rag.build_index(chunks)

    query = st.text_input("Ask a question:")
    if st.button("Submit") and query:
        with st.spinner("Generating answer..."):
            answer = rag.generate_answer(query)
        st.subheader("Answer")
        st.write(answer)
else:
    st.warning("Please upload at least one PDF file.")