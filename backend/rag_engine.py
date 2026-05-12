
# =========================
# FILE: backend/rag_engine.py
# =========================

import os
import pandas as pd

from backend.vector_store import (
    collection,
    model
)

# =========================
# DATA PATH
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
# SEMANTIC SEARCH
# =========================

def semantic_food_search(
    query,
    top_k=3
):

    query_embedding = model.encode(
        [query]
    )[0].tolist()

    results = collection.query(

        query_embeddings=[
            query_embedding
        ],

        n_results=top_k
    )

    matched_ids = results["ids"][0]

    output = []

    for idx in matched_ids:

        row = food_db.iloc[
            int(idx)
        ]

        output.append({

            "food": str(
                row.get(
                    FOOD_COLUMN,
                    ""
                )
            ),

            "calories": float(
                row.get(
                    "Calories (kcal)",
                    0
                )
            ),

            "protein": float(
                row.get(
                    "Protein (g)",
                    0
                )
            ),

            "carbs": float(
                row.get(
                    "Carbohydrates (g)",
                    0
                )
            ),

            "fat": float(
                row.get(
                    "Fats (g)",
                    0
                )
            ),

            "fiber": float(
                row.get(
                    "Fibre (g)",
                    0
                )
            )
        })

    return output

