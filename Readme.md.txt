# ⚖️ RAG Legal Q&A Chatbot

A legal document question-answering chatbot using Retrieval-Augmented Generation (RAG) with OpenAI, LangChain, and FAISS. Upload a PDF legal document and ask anything from it!

---

## 🚀 Features

- 📄 Upload legal PDFs
- 🔍 Extract answers from docs using RAG
- 🤖 GPT-4 powered responses
- 💾 Embed and search with FAISS
- 📦 Built with LangChain, OpenAI, and Streamlit

---

## 🛠️ Tech Stack

- Python 3.11+
- LangChain
- OpenAI API (GPT-4)
- FAISS (Vector DB)
- PyPDF2
- Streamlit (for UI)

---

## 📦 Setup

1. **Clone the repo**

```bash
git clone https://github.com/your-username/rag-legal-qa-bot.git
cd rag-legal-qa-bot
2. INSTALL DEPENDENCIES
pip install -r requirements.txt
3.ADD YOUR OPEN API KEY 
cp .env.example .env
# Then edit .env and add your key
4. RUN THE APP
streamlit run app.py
## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.