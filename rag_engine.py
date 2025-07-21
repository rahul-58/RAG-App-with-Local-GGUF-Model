import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from llama_cpp import Llama

class RAGPipeline:
    def __init__(self, model_path: str):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.model_path = model_path
        self.chunks = []
        self.index = None

    def build_index(self, chunks):
        self.chunks = chunks
        embeddings = self.embedder.encode(chunks, show_progress_bar=True)
        index = faiss.IndexFlatL2(embeddings.shape[1])
        index.add(np.array(embeddings))
        self.index = index

    def retrieve(self, query, k=5):
        query_embedding = self.embedder.encode([query])
        D, I = self.index.search(np.array(query_embedding), k)
        return [self.chunks[i] for i in I[0]]

    def generate_answer(self, query):
        retrieved_chunks = self.retrieve(query)
        context = "\n".join(retrieved_chunks)
        prompt = f"""You are a helpful assistant. Use the context below to answer the question.\n
        Context:\n{context}\n
        Question: {query}\n
        Answer:"""

        llm = Llama(model_path=self.model_path, n_ctx=2048)
        output = llm(prompt, max_tokens=512, stop=["\n"])
        return output["choices"][0]["text"].strip()