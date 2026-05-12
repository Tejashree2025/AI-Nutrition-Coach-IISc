from sentence_transformers import SentenceTransformer
import numpy as np

# load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_text(text):
    try:
        vec = model.encode(text)

        vec = np.array(vec).astype("float32")

        norm = np.linalg.norm(vec)

        # 🔥 CRITICAL FIX
        if norm == 0:
            return vec

        return vec / norm

    except Exception as e:
        print("EMBED ERROR:", e)
        return np.zeros(384).astype("float32")  # safe fallback