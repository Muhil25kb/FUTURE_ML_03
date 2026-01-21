import pandas as pd

df = pd.read_csv("chat_datasets/personality.csv")

pairs = []

for row in df["chat"].dropna():
    lines = row.split("\n")

    for i in range(len(lines) - 1):
        q = lines[i].strip().lower()
        a = lines[i + 1].strip().lower()

        if len(q) > 2 and len(a) > 2:
            pairs.append([q, a])

out = pd.DataFrame(pairs, columns=["question", "response"])
out.to_csv("chat_datasets/persona_clean.csv", index=False)

print("Persona pairs:", len(out))
