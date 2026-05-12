
# =========================
# FILE: backend/vector_store.py
# =========================

import os
import pandas as pd
import chromadb

from sentence_transformers import (
    SentenceTransformer
)

# =========================
# LOAD EMBEDDING MODEL
# =========================

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# =========================
# CHROMADB
# =========================

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="food_embeddings"
)

# =========================
# DATASET PATH
# =========================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "datasets",
    "Indian_Food_Nutrition_Processed.csv"
)

# =========================
# LOAD DATASET
# =========================

food_db = pd.read_csv(DATA_PATH)

food_db.columns = [
    col.strip()
    for col in food_db.columns
]

# =========================
# DETECT FOOD COLUMN
# =========================

FOOD_COLUMN = None

possible_columns = [
    "Food",
    "food",
    "Dish Name",
    "Dish_Name",
    "dish_name",
    "Name"
]

for col in possible_columns:

    if col in food_db.columns:

        FOOD_COLUMN = col
        break

if FOOD_COLUMN is None:

    FOOD_COLUMN = food_db.columns[0]

# =========================
# BUILD VECTOR DATABASE
# =========================

def build_vector_database():

    existing = collection.count()

    if existing > 0:

        return

    documents = []

    ids = []

    embeddings = []

    for idx, row in food_db.iterrows():

        food_name = str(
            row[FOOD_COLUMN]
        )

        documents.append(food_name)

        ids.append(str(idx))

        embedding = model.encode(
            food_name
        ).tolist()

        embeddings.append(
            embedding
        )

    collection.add(

        documents=documents,

        embeddings=embeddings,

        ids=ids
    )

    print(
        "✅ ChromaDB food embeddings created"
    )

# =========================
# INITIALIZE
# =========================

build_vector_database()

