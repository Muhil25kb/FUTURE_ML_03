import pandas as pd

df = pd.read_csv("chat_datasets/persona_clean.csv")

bad_words = ["kill", "fight", "hate", "die", "gun", "bomb", "movie", "song"]

def clean(q, a):
    text = (q + " " + a).lower()
    if any(b in text for b in bad_words):
        return False
    if len(q) > 100 or len(a) > 100:
        return False
    return True

filtered = df[df.apply(lambda x: clean(x["question"], x["response"]), axis=1)]

filtered.to_csv("chat_datasets/persona_support.csv", index=False)

print("Filtered Persona:", len(filtered))
