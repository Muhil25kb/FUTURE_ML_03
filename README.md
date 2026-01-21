🤖 Customer Support Chatbot

A Smart Customer Support Chatbot built using FastAPI, Sentence Transformers, and Streamlit.
The bot can handle greetings, small talk, refunds, order tracking, and product information, with intelligent fallback responses powered by trained datasets.

🚀 Features

✅ Greeting & Small Talk Handling (hi, hello, thanks, okay, bye, etc.)

💰 Refund Request Flow with Order ID Detection

📦 Order Tracking Flow

📱 Product Information Support (example: Samsung phones)

🧠 Persona-based conversational responses

🔎 Semantic Search using Sentence Transformers

🌐 Web UI built with Streamlit

⚡ FastAPI backend with session memory

🧠 How It Works

User enters a message via the Streamlit web UI

Request is sent to the FastAPI backend

Backend performs:

Greeting / small-talk detection

Intent classification (refund, tracking, product)

Order ID extraction

Persona & dataset-based fallback

A relevant response is returned to the UI

🗂️ Project Structure
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

🧠 Models Used

SentenceTransformer – all-MiniLM-L6-v2

PersonaChat dataset – for natural conversational replies

TWCS dataset – for customer support–style responses

📦 Datasets

PersonaChat Dataset – casual conversation & personality-based replies

TWCS (Twitter Customer Support) – support-style responses

Custom Product Dataset (for phone/product info)

🛠️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/customer-support-chatbot.git
cd customer-support-chatbot

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


Required libraries:

fastapi

uvicorn

streamlit

pandas

joblib

sentence-transformers

tensorflow

▶️ Running the Project
Start Backend (FastAPI)
cd backend
uvicorn main:app --reload


Backend runs on:

http://127.0.0.1:8000

Start Frontend (Streamlit)
cd web
streamlit run app.py


Web UI runs on:

http://localhost:8501
