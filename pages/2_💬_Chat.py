import streamlit as st

from utils.chatbot import ask_gemini

from utils.chat_history import (
    save_conversation,
    load_conversations,
    delete_history
)

from utils.session_manager import (
    initialize_session,
    create_new_session,
    get_current_session,
    switch_session,
    remove_session
)

from utils.database import get_chat_sessions
from utils.pdf_manager import get_document_names


# =====================================================
# Page Title
# =====================================================

st.title("💬 AI PDF Chat")
st.caption("Ask questions about your uploaded PDF documents.")

initialize_session()

current_session = get_current_session()

# =====================================================
# Sidebar - Chat Sessions
# =====================================================

st.sidebar.title("💬 Chats")

# -------------------------
# Create New Chat
# -------------------------

if st.sidebar.button("➕ New Chat"):

    create_new_session()

    st.session_state.messages = []

    st.rerun()

st.sidebar.divider()

# -------------------------
# Chat List
# -------------------------

sessions = get_chat_sessions()

for session_id, session_name in sessions:

    if st.sidebar.button(
        f"📄 {session_name}",
        key=f"session_{session_id}"
    ):

        switch_session(session_id)

        if "messages" in st.session_state:
            del st.session_state.messages

        st.rerun()

st.sidebar.divider()

# =====================================================
# Sidebar - Search Settings
# =====================================================

documents = get_document_names()

selected_document = st.sidebar.selectbox(
    "🔍 Search In",
    ["All Documents"] + documents
)

if selected_document == "All Documents":
    selected_document = None

st.sidebar.divider()

# =====================================================
# Sidebar - Chat Actions
# =====================================================

if st.sidebar.button("🧹 Clear Chat History"):

    delete_history(current_session)

    st.session_state.messages = []

    st.rerun()

if st.sidebar.button("🗑 Delete Current Chat"):

    remove_session(current_session)

    if "messages" in st.session_state:
        del st.session_state.messages

    st.rerun()

# =====================================================
# Load Chat History
# =====================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

    history = load_conversations(current_session)

    for question, answer, created_at in history:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }

        )

# =====================================================
# Display Previous Messages
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =====================================================
# Chat Input
# =====================================================

question = st.chat_input(
    "Ask something about your PDFs..."
)

if question:

    # -------------------------
    # User Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # -------------------------
    # Assistant Response
    # -------------------------

    with st.chat_message("assistant"):

        with st.spinner("Searching documents..."):

            answer, sources = ask_gemini(
                question,
                selected_document
            )

        st.markdown(answer)

        if sources:

            st.divider()

            st.markdown("### 📚 Sources")

            for source in sources:

                st.markdown(
                    f"- **{source['file']}** — Page {source['page']}"
                )

    # -------------------------
    # Save Assistant Message
    # -------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # -------------------------
    # Save Conversation
    # -------------------------

    save_conversation(
        current_session,
        question,
        answer
    )