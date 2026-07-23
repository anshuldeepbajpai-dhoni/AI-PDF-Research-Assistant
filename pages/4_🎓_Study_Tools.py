import streamlit as st

from utils.pdf_manager import get_document_names

from utils.study_tools import (
    generate_summary,
    generate_notes,
    generate_flashcards,
    generate_mcqs,
    generate_interview_questions
)
from utils.interactive_tools import (
    render_flashcards,
    render_mcq,
    render_interview
)

st.set_page_config(
    page_title="AI Study Tools",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI Study Tools")
st.caption(
    "Generate AI-powered learning material from your PDF documents."
)

# =====================================================
# Document Selection
# =====================================================

documents = get_document_names()

selected_document = st.selectbox(
    "📄 Select Document",
    ["All Documents"] + documents
)

if selected_document == "All Documents":
    selected_document = None

st.divider()

# =====================================================
# Tool Cards
# =====================================================

col1, col2 = st.columns(2)

# =====================================================
# Executive Summary
# =====================================================

with col1:

    with st.container(border=True):

        st.subheader("📄 Executive Summary")

        st.write(
            "Generate a concise executive summary."
        )

        if st.button(
            "Generate Summary",
            use_container_width=True
        ):

            with st.spinner("Generating..."):

                st.session_state.study_output = (
                    "📄 Executive Summary",
                    generate_summary(
                        selected_document,
                        "executive"
                    )
                )

# =====================================================
# Study Notes
# =====================================================

with col2:

    with st.container(border=True):

        st.subheader("📝 Study Notes")

        st.write(
            "Generate structured study notes."
        )

        if st.button(
            "Generate Notes",
            use_container_width=True
        ):

            with st.spinner("Generating..."):

                st.session_state.study_output = (
                    "📝 Study Notes",
                    generate_notes(
                        selected_document
                    )
                )

# =====================================================
# Flashcards
# =====================================================

col3, col4 = st.columns(2)

with col3:

    with st.container(border=True):

        st.subheader("🧠 Flashcards")

        st.write(
            "Create revision flashcards."
        )

        if st.button(
            "Generate Flashcards",
            use_container_width=True
        ):

            with st.spinner("Generating..."):

                st.session_state.study_output = (
                    "🧠 Flashcards",
                    generate_flashcards(
                        selected_document
                    )
                )

with col4:

    with st.container(border=True):

        st.subheader("❓ MCQs")

        st.write(
            "Generate practice MCQs."
        )

        if st.button(
            "Generate MCQs",
            use_container_width=True
        ):

            with st.spinner("Generating..."):

                st.session_state.study_output = (
                    "❓ MCQs",
                    generate_mcqs(
                        selected_document
                    )
                )

# =====================================================
# Interview Questions
# =====================================================

with st.container(border=True):

    st.subheader("💼 Interview Questions")

    st.write(
        "Generate interview questions with answers."
    )

    if st.button(
        "Generate Interview Questions",
        use_container_width=True
    ):

        with st.spinner("Generating..."):

            st.session_state.study_output = (
                "💼 Interview Questions",
                generate_interview_questions(
                    selected_document
                )
            )

# =====================================================
# Output Workspace
# =====================================================

if "study_output" in st.session_state:

    title, content = st.session_state.study_output

    st.divider()

    preview_tab, download_tab = st.tabs(
        [
            "📑 Preview",
            "📥 Download"
        ]
    )

    with preview_tab:

        st.subheader(title)

        if "Flashcards" in title:

            render_flashcards(content)

        elif "MCQ" in title:

            render_mcq(content)

        elif "Interview" in title:

            render_interview(content)

        else:

            st.markdown(content)

        st.download_button(
            "📄 Download Markdown",
            content,
            file_name="study_output.md",
            mime="text/markdown",
            use_container_width=True
        )

    with download_tab:

        st.info(
            "More export formats will be available in the next phase."
        )

        st.code(content)