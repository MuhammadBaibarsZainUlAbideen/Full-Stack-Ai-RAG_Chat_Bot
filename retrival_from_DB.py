import faiss, pickle, numpy as np
from sentence_transformers import SentenceTransformer

index = faiss.read_index("faiss.index")
meta = pickle.load(open("faiss_meta.pkl","rb"))
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, k=5):
    qv = embed_model.encode([query]).astype("float32")
    D,I = index.search(qv, k)
    results = [meta[i] for i in I[0]]
    return results
