import pandas as pd
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

print("📥 Loading personality dataset...")

df = pd.read_csv("chat_datasets/personality.csv")

# Keep only valid rows
df = df[["Persona", "chat"]].dropna()

pairs = []

for row in df["chat"]:
    parts = row.split("\n")
    for i in range(len(parts) - 1):
        q = parts[i].strip()
        a = parts[i + 1].strip()
        if len(q) > 3 and len(a) > 3:
            pairs.append((q, a))

data = pd.DataFrame(pairs, columns=["question", "response"])

print("Total persona pairs:", len(data))

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode questions
embeddings = model.encode(data["question"].tolist(), show_progress_bar=True)

# Save model
joblib.dump((model, embeddings, data), "chat_datasets/personality_model.pkl")

print("✅ PersonaChat model saved!")
