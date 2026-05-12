
# =========================
# FILE: embedding_builder.py
# =========================

import pandas as pd
import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

# =========================
# LOAD DATASET
# =========================

df = pd.read_csv(
    "Indian_Food_Nutrition_Processed.csv"
)

# =========================
# FOOD COLUMN
# =========================

FOOD_COLUMN = "Dish Name"

# =========================
# CLEAN DATA
# =========================

df = df.fillna(0)

foods = df[FOOD_COLUMN].astype(str).tolist()

# =========================
# LOAD MODEL
# =========================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =========================
# CREATE EMBEDDINGS
# =========================

embeddings = model.encode(
    foods,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

# =========================
# CREATE FAISS INDEX
# =========================

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

# =========================
# SAVE INDEX
# =========================

faiss.write_index(
    index,
    "rag/food_index.faiss"
)

# =========================
# SAVE METADATA AS LIST
# =========================

metadata = df.to_dict(
    orient="records"
)

with open(
    "rag/food_meta.pkl",
    "wb"
) as f:

    pickle.dump(
        metadata,
        f
    )

# =========================
# DONE
# =========================

print(
    "✅ FAISS embeddings created successfully"
)

