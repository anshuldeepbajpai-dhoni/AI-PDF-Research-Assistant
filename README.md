# 🧠 AI PDF Research Assistant

> An intelligent AI-powered PDF Research Assistant built with **Streamlit, LangChain, ChromaDB, Google Gemini, and SQLite**. Upload multiple PDFs, chat with them using Retrieval-Augmented Generation (RAG), generate study materials, export conversations, and analyze your document library through an interactive dashboard.

---

# ✨ Features

## 📄 Document Management

- Upload multiple PDF documents
- OCR support for scanned PDFs
- Automatic text extraction and chunking
- Embedding generation
- ChromaDB vector storage
- Delete PDFs from storage and vector database
- Multi-document management

---

## 🤖 AI Chat

- Google Gemini powered conversations
- Retrieval-Augmented Generation (RAG)
- Hybrid Search (Semantic + BM25)
- Search across all documents
- Search within a specific PDF
- Context-aware prompt building
- Source citations with page numbers
- Persistent chat history
- Multiple chat sessions

---

## 🎓 AI Study Tools

- AI Notes Generator
- Flashcard Generator
- Quiz Generator
- Interview Question Generator
- MCQ Generator

---

## 📊 Analytics Dashboard

- Total Documents
- Total Pages
- Total Chunks
- Storage Usage
- Pages per PDF
- Chunks per PDF
- Upload Timeline
- Storage Distribution
- Interactive Charts

---

## 📤 Export

- Export Chat as PDF
- Export Chat as DOCX
- Export Chat as Markdown

---

## 💾 Database

- SQLite metadata storage
- Persistent chat history
- Persistent chat sessions
- Document metadata
- Analytics metadata

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

## Search

- Semantic Search
- BM25 Search
- Hybrid Retrieval

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

├── app.py
├── assets/
│   ├── style.css
│   ├── logo.png
│   └── icons/
│
├── pages/
│   ├── 1_📄_Documents.py
│   ├── 2_💬_Chat.py
│   ├── 3_📊_Analytics.py
│   ├── 4_🎓_Study_Tools.py
│   └── 5_⚙️_Settings.py
│
├── utils/
│   ├── analytics.py
│   ├── bm25.py
│   ├── chatbot.py
│   ├── chat_history.py
│   ├── citations.py
│   ├── database.py
│   ├── embeddings.py
│   ├── export.py
│   ├── hybrid_search.py
│   ├── interactive_tools.py
│   ├── loader.py
│   ├── memory.py
│   ├── ocr.py
│   ├── pdf_manager.py
│   ├── pdf_viewer.py
│   ├── prompt_builder.py
│   ├── reranker.py
│   ├── session_manager.py
│   ├── splitter.py
│   ├── study_tools.py
│   ├── theme.py
│   └── vectordb.py
│
├── chroma_db/
├── database/
│   └── chat.db
├── pdfs/
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

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

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
- OCR Processing
- Delete PDFs
- Automatic Indexing
- ChromaDB Storage

---

## 💬 Chat

- AI-powered conversations
- Hybrid Search
- Multiple chat sessions
- Persistent history
- Source citations
- Search specific PDF
- Search all PDFs

---

## 📊 Analytics

- Document statistics
- Storage analytics
- Upload trends
- Interactive charts

---

## 🎓 Study Tools

- Notes Generator
- Flashcards
- Quiz Generator
- Interview Questions
- MCQs

---

## ⚙️ Settings

- Application configuration
- Theme settings
- Model settings

---

# 📈 Current Features

| Feature | Status |
|---------|:------:|
| Multi PDF Upload | ✅ |
| OCR Support | ✅ |
| Semantic Search | ✅ |
| BM25 Search | ✅ |
| Hybrid Search | ✅ |
| Google Gemini Integration | ✅ |
| ChromaDB Vector Store | ✅ |
| LangChain Pipeline | ✅ |
| Persistent Chat History | ✅ |
| Multi-Session Chat | ✅ |
| SQLite Database | ✅ |
| Analytics Dashboard | ✅ |
| Source Citations | ✅ |
| Search Specific PDF | ✅ |
| Search Across PDFs | ✅ |
| AI Notes Generator | ✅ |
| Flashcard Generator | ✅ |
| Quiz Generator | ✅ |
| Interview Questions | ✅ |
| Chat Export (PDF/DOCX/Markdown) | ✅ |
| Premium UI | ✅ |

---

# 🚀 Upcoming Features (Phase 9)

- ⚡ Streaming AI Responses
- 🧠 Long-Term Memory
- 🎯 Cross-Encoder Reranking
- 🎤 Voice Chat
- 📌 PDF Highlight Navigation
- 🔍 Conversation Search
- 📚 AI Research Timeline
- 🤖 Autonomous AI Research Agent

---

# 📸 Screenshots

Add screenshots for:

- 🏠 Home Page
- 📄 Documents Page
- 💬 Chat Interface
- 📊 Analytics Dashboard
- 🎓 Study Tools
- 📝 AI Notes
- 🧠 Flashcards
- ❓ Quiz Generator

---

# ⭐ Highlights

- 🚀 Production-Ready RAG Architecture
- 🧠 Hybrid Retrieval (Semantic + BM25)
- 📚 AI Study Assistant
- 💬 Multi-Session Chat
- 📊 Analytics Dashboard
- 📤 Export Support
- 📄 OCR Enabled
- 🎨 Premium UI
- ⚡ Fast ChromaDB Search

---

# 🛣️ Roadmap

- ✅ Phase 1 — Project Setup
- ✅ Phase 2 — Multi-PDF Upload
- ✅ Phase 3 — OCR Integration
- ✅ Phase 4 — ChromaDB Integration
- ✅ Phase 5 — Gemini Chat
- ✅ Phase 6 — Chat History & Export
- ✅ Phase 7 — AI Study Tools
- ✅ Phase 8 — Hybrid Search & Premium UI
- 🚀 Phase 9 — Production AI Research Assistant

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to GitHub

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
- LinkedIn: https://www.linkedin.com/in/anshul-deep-bajpai-441b1b37b/

---

## ⭐ If you found this project useful, consider giving it a star on GitHub!