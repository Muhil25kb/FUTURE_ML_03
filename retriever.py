def get_dataset_reply(text):
    try:
        if not text or len(text.strip()) < 2:
            return None

        emb = chat_model.encode([text])
        scores = cosine_similarity(emb, chat_embeddings)

        idx = scores.argmax()
        confidence = scores[0][idx]

        # ❗ IMPORTANT threshold
        if confidence < 0.45:
            return None

        return chat_df.iloc[idx]["response"]

    except Exception as e:
        print("Retriever error:", e)
        return None
