import os
import shutil
import streamlit as st

from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.vectordb import create_vector_db, load_vector_db
from utils.chatbot import ask_gemini


st.set_page_config(
    page_title="AI PDF Research Assistant",
    page_icon="📚",
    layout="wide"
)


if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("📚 AI PDF Research Assistant")
st.markdown("---")


with st.sidebar:

    st.header("Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        os.makedirs("pdfs", exist_ok=True)

        pdf_path = os.path.join("pdfs", uploaded_file.name)

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        with st.spinner("Reading PDF..."):

            docs = load_pdf(pdf_path)

            chunks = split_documents(docs)

            create_vector_db(chunks)

            st.session_state.db_ready = True

        st.success("PDF Indexed Successfully")

    st.divider()

    if st.button("Clear Database"):

        if os.path.exists("chroma_db"):
            shutil.rmtree("chroma_db")

        st.session_state.db_ready = False
        st.session_state.chat_history = []

        st.success("Database Cleared")


if st.session_state.db_ready:

    question = st.chat_input("Ask something about your PDF")

    if question:

        db = load_vector_db()

        docs = db.similarity_search(question, k=4)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        answer = ask_gemini(question, context)

        st.session_state.chat_history.append(
            ("You", question)
        )

        st.session_state.chat_history.append(
            ("AI", answer)
        )


for role, message in st.session_state.chat_history:

    if role == "You":

        with st.chat_message("user"):
            st.write(message)

    else:

        with st.chat_message("assistant"):
            st.write(message)

else:

    if not st.session_state.db_ready:

        st.info("Upload a PDF from the sidebar to begin.")