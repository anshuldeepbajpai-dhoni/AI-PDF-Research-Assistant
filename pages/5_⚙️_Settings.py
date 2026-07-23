import streamlit as st

st.title("⚙ Settings")

st.selectbox(
    "LLM",
    [
        "Gemini Flash",
        "Gemini Pro"
    ]
)

st.selectbox(
    "Embedding Model",
    [
        "MiniLM"
    ]
)

st.toggle("Dark Mode",True)