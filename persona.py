import joblib
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

print("🧠 Loading PersonaChat model...")

MODEL_PATH = "chat_datasets/personality_model.pkl"  # ✅ CORRECT PATH

try:
    model, embeddings, df = joblib.load(MODEL_PATH)
except Exception as e:
    print("❌ Persona model load failed:", e)
    model, embeddings, df = None, None, None


def get_persona_reply(text):
    if model is None:
        return "Hello! How can I help you today?"

    q_emb = model.encode([text])
    sims = cosine_similarity(q_emb, embeddings)[0]
    idx = int(np.argmax(sims))

    if sims[idx] > 0.45:
        return str(df.iloc[idx]["response"])

    return "Hello! How can I help you today?"
