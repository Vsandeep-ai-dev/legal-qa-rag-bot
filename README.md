# 🤖 Legal Q&A RAG Bot

An AI-powered Legal Question-Answering system that uses Retrieval-Augmented Generation (RAG) to provide accurate responses from a legal document database. It combines LangChain, vector embeddings, and OpenAI’s GPT models to ensure reliable legal answers.

---

## 🚀 Features

- ✅ **Ask Legal Questions** – Get answers based on actual legal documents.
- ✅ **Retrieval-Augmented Generation (RAG)** – Combines document context with GPT for accuracy.
- ✅ **LangChain Integration** – Handles document loading, chunking, and chaining.
- ✅ **Embedding + Vector Store** – Converts documents into vectors for semantic search.
- ✅ **Simple Streamlit UI** – Easy-to-use web interface.
- ✅ **OpenAI GPT** – Powered by GPT-3.5/4 for final response generation.

---

## 📁 Project Structure

```
legal-qa-rag-bot/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── app.py                # Streamlit app UI
├── qa_chain.py           # LangChain question-answering logic
├── vector_store.py       # Vector DB (FAISS) logic
├── data/
│   └── legal_docs/       # Upload your PDF/DOCX legal files here
├── .env                  # API keys (DO NOT COMMIT)
```

---

## 🛠️ Tech Stack

- **Python 3.11+**
- **LangChain**
- **FAISS (Facebook AI Similarity Search)**
- **OpenAI GPT-3.5/4**
- **Streamlit** for UI
- **python-dotenv**

---

## ▶️ How to Run

1. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up `.env` file:**

Create a `.env` file in the root with this line:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

4. **Add Legal Documents:**

Place your `.pdf` or `.docx` files inside the `data/legal_docs/` folder.

5. **Run the app:**

```bash
streamlit run app.py
```

---

## ✅ Best Practices

- **Never commit `.env` or API keys.**
- Add this to your `.gitignore` file:

```
.env
```

- Clean up large or unnecessary files before pushing.

---

## 🧪 Testing & Output

- Ask natural language legal questions.
- Answers will be based only on your uploaded documents.
- Everything happens locally except OpenAI API calls.

---

## 💡 Future Enhancements

- 🔐 Authentication for private deployments
- 📊 Admin dashboard for monitoring usage
- 💬 Chat history + feedback collection
- 🌍 Multi-language support
- 🧠 Plug into government APIs or court data

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss the improvements you'd like to make.

---

## 📸 Demo Screenshot (Optional)

```
Place your demo images or gifs in a `screenshots/` folder and reference like:

![App Screenshot](screenshots/demo.png)
```

---

## 🔗 Useful Commands

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/legal-qa-rag-bot.git
git push -u origin main
```

---

