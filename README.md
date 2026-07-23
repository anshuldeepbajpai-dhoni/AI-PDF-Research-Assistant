# 🧠 AI PDF Research Assistant

> An intelligent AI-powered PDF research assistant built with **Streamlit, LangChain, ChromaDB, Google Gemini, and SQLite**. Upload multiple PDFs, chat with them using Retrieval-Augmented Generation (RAG), manage multiple conversations, and analyze your document library through an interactive dashboard.

---

## ✨ Features

### 📄 Document Management
- Upload multiple PDF documents
- Automatic text extraction and chunking
- Semantic embedding generation
- ChromaDB vector storage
- Delete documents from storage and vector database
- Multi-document management

### 🤖 AI Chat
- Chat with uploaded PDFs using Google Gemini
- Retrieval-Augmented Generation (RAG)
- Search across all documents
- Search within a specific document
- Source citations with page numbers
- Persistent chat history
- Multiple chat sessions

### 📊 Analytics Dashboard
- Total documents
- Total pages
- Total chunks
- Storage usage
- Pages per PDF
- Chunks per PDF
- Upload timeline
- Storage distribution charts

### 💾 Database
- SQLite metadata storage
- Persistent chat history
- Persistent chat sessions
- Document metadata management

---

# 🚀 Tech Stack

## Frontend
- Streamlit

## Backend
- Python 3.11

## AI & NLP
- Google Gemini
- LangChain
- Sentence Transformers

## Vector Database
- ChromaDB

## Database
- SQLite

## Visualization
- Plotly
- Pandas

---

# 📂 Project Structure

```text
AI-PDF-Research-Assistant/

│
├── app.py
│
├── assets/
│
├── pages/
│   ├── 1_📄_Documents.py
│   ├── 2_💬_Chat.py
│   ├── 3_📊_Analytics.py
│   └── 4_⚙️_Settings.py
│
├── utils/
│   ├── analytics.py
│   ├── chatbot.py
│   ├── chat_history.py
│   ├── database.py
│   ├── embeddings.py
│   ├── loader.py
│   ├── pdf_manager.py
│   ├── session_manager.py
│   ├── splitter.py
│   └── vectordb.py
│
├── pdfs/
├── chroma_db/
├── database/
│   └── chat.db
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/anshuldeepbajpai-dhoni/AI-PDF-Research-Assistant.git

cd AI-PDF-Research-Assistant
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## Run the Application

```bash
streamlit run app.py
```

---

# 🖥️ Application Modules

## 📄 Documents
- Upload PDFs
- Delete PDFs
- Automatic indexing
- ChromaDB storage

---

## 💬 Chat

- AI-powered conversations
- Multiple chat sessions
- Persistent history
- Source references
- Search one or all documents

---

## 📊 Analytics

- Document statistics
- Storage analytics
- Upload trends
- Interactive charts

---

## ⚙️ Settings

- Application configuration
- Future customization options

---

# 📈 Current Features

- ✅ Multi PDF Upload
- ✅ Semantic Search
- ✅ Google Gemini Integration
- ✅ ChromaDB Vector Store
- ✅ LangChain Pipeline
- ✅ Multi-Session Chat
- ✅ Persistent Chat History
- ✅ SQLite Database
- ✅ Analytics Dashboard
- ✅ Source Citations
- ✅ Search Specific PDF
- ✅ Search Across All PDFs

---

# 🚧 Upcoming Features

- OCR Support for Scanned PDFs
- Export Chat (PDF / DOCX / Markdown)
- AI Notes Generator
- Flashcard Generator
- Quiz Generator
- MCQ Generator
- Hybrid Search (BM25 + Semantic Search)
- Dark Mode
- Modern UI
- AI Research Agent

---

# 📸 Screenshots

> Add screenshots of:
- Documents Page
- Chat Page
- Analytics Dashboard
- Multiple Chat Sessions

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Add new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Anshul Deep Bajpai**

- GitHub: https://github.com/anshuldeepbajpai-dhoni
- LinkedIn: www.linkedin.com/in/anshul-deep-bajpai-441b1b37b

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!