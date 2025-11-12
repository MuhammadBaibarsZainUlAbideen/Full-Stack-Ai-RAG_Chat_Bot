from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

file_path = "harvard_cleaned.txt" 

with open(file_path, "r", encoding="utf-8") as file:
    lines = []
    for i, line in enumerate(file):
        if i == 565:  
            break
        lines.append(line.strip())
b = ""
for ff in lines:
    b += ff

chunk_zie = 100
overlap = 10
nl = []
for j in range(0,len(b),chunk_zie-overlap):
    chunks = b[j:j+chunk_zie]
    nl.append(chunks)

model = SentenceTransformer("all-MiniLM-L6-v2")
embs = model.encode(nl, convert_to_numpy=True, show_progress_bar=True)
dim = embs.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embs.astype("float32"))
faiss.write_index(index, "faiss.index")
pickle.dump(nl, open("faiss_meta.pkl", "wb"))