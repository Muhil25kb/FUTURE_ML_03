import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer

df = pd.read_csv("twcs.csv")

# Clean dataset
df = df[df["text"].notna()]
df["clean_text"] = df["text"].str.replace(r"@\w+", "", regex=True)

questions = df["clean_text"].tolist()

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(questions, show_progress_bar=True)

joblib.dump((model, embeddings, df), "model.pkl")

print("✅ New smart local model trained")
