
# 🤖 Customer Support Chatbot

A **smart AI-powered Customer Support Chatbot** built using **FastAPI**, **Sentence Transformers**, and **Streamlit**.
The chatbot handles greetings, small talk, refunds, order tracking, and product-related queries, with intelligent fallback responses powered by trained conversational datasets.

---

## 🚀 Features

✅ Greeting & Small Talk Handling
*(hi, hello, thanks, okay, bye, etc.)*

💰 Refund Request Flow with **Order ID Detection**

📦 Order Tracking Flow

📱 Product Information Support
*(example: Samsung phones)*

🧠 Persona-based Conversational Responses

🔎 Semantic Search using **Sentence Transformers**

🌐 Interactive Web UI built with **Streamlit**

⚡ **FastAPI backend** with session memory

---

## 🧠 How It Works

1. User enters a message via the **Streamlit Web UI**
2. Request is sent to the **FastAPI backend**
3. Backend processes the input by:

   * Greeting / small-talk detection
   * Intent classification (refund, tracking, product info)
   * Order ID extraction
   * Persona-based and dataset-driven fallback responses
4. A relevant response is returned to the UI

---

## 🗂️ Project Structure

```
support_bot/
│
├── backend/
│   ├── chat_datasets/
│   │   ├── personality.csv
│   │   ├── persona_clean.csv
│   │   ├── persona_support.csv
│   │   ├── personality_model.pkl
│   │
│   ├── intent.py
│   ├── utils.py
│   ├── retriever.py
│   ├── persona.py
│   ├── products.py
│   ├── product_handler.py
│   ├── train_chatbot.py
│   ├── main.py
│   └── model.pkl
│
├── web/
│   └── app.py
│
├── run_all.py
├── twcs.csv
└── README.md
```

---

## 🧠 Models Used

* **SentenceTransformer** – `all-MiniLM-L6-v2`
* **PersonaChat Dataset** – for natural conversational replies
* **TWCS Dataset** – for customer support–style responses

---

## 📦 Datasets

* **PersonaChat Dataset** – casual conversation & persona-based replies
* **TWCS (Twitter Customer Support)** – customer support interactions
* **Custom Product Dataset** – phone & product information

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Libraries

* fastapi
* uvicorn
* streamlit
* pandas
* joblib
* sentence-transformers
* tensorflow

---

## ▶️ Running the Project

### 🔹 Start Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

📍 Backend URL:

```
http://127.0.0.1:8000
```

---

### 🔹 Start Frontend (Streamlit)

```bash
cd web
streamlit run app.py
```

📍 Web UI URL:

```
http://localhost:8501
```

## 📌 Conclusion

This project demonstrates how **semantic search, intent detection, and persona-based conversational AI** can be combined to build a **real-world customer support chatbot**.
It showcases backend API design, NLP-based retrieval, and frontend integration suitable for production-grade support systems.


