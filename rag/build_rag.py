import faiss
import pickle
import chromadb
import pandas as pd
import numpy as np

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

food_db = pd.read_csv(
    "Indian_Food_Nutrition_Processed.csv"
)

food_db = food_db.fillna(0)

food_texts = []
metadata = []

for _, row in food_db.iterrows():

    text = f"""
Food: {row.get('Dish Name', '')}
Calories: {row.get('Calories (kcal)', 0)}
Protein: {row.get('Protein (g)', 0)}
Carbs: {row.get('Carbohydrates (g)', 0)}
Fat: {row.get('Fats (g)', 0)}
Fiber: {row.get('Fibre (g)', 0)}
"""

    food_texts.append(text)

    metadata.append({
        "food": row.get("Dish Name", "Unknown"),
        "calories": float(row.get("Calories (kcal)", 0)),
        "protein": float(row.get("Protein (g)", 0)),
        "carbs": float(row.get("Carbohydrates (g)", 0)),
        "fat": float(row.get("Fats (g)", 0)),
        "fiber": float(row.get("Fibre (g)", 0))
    })

embeddings = model.encode(
    food_texts,
    show_progress_bar=True
)

embeddings = np.array(
    embeddings,
    dtype="float32"
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(embeddings)

faiss.write_index(
    index,
    "rag/food_index.faiss"
)

with open(
    "rag/food_meta.pkl",
    "wb"
) as f:

    pickle.dump(metadata, f)

client = chromadb.PersistentClient(
    path="rag/chroma_db"
)

collection = client.get_or_create_collection(
    name="nutrition"
)

for i, text in enumerate(food_texts):

    collection.add(
        documents=[text],
        ids=[str(i)]
    )

print("RAG Database Created Successfully")