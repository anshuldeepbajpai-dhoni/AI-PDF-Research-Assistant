import streamlit as st
from utils.database import initialize_database

initialize_database()

st.set_page_config(
    page_title="AI PDF Research Assistant",
    page_icon="📚",
    layout="wide"
)

with open("assets/style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.title("📚 AI PDF Research Assistant")

st.write("Welcome to the dashboard.")

c1,c2,c3,c4=st.columns(4)

c1.metric("Documents","0")
c2.metric("Pages","0")
c3.metric("Chunks","0")
c4.metric("Questions","0")

st.divider()

st.info("Use the left sidebar to navigate.")