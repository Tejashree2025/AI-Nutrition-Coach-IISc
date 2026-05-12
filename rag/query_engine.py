import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

# =========================
# LOAD MODEL
# =========================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =========================
# LOAD FAISS INDEX
# =========================

index = faiss.read_index(
    "rag/food_index.faiss"
)

# =========================
# LOAD METADATA
# =========================

with open(
    "rag/food_meta.pkl",
    "rb"
) as f:

    metadata = pickle.load(f)

# =========================
# SEARCH FUNCTION
# =========================

def search_food(
    query,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:

        if idx < len(metadata):

            results.append(
                metadata[idx]
            )

    return results