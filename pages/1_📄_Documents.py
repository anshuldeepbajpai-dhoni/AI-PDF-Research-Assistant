import os
import streamlit as st

from utils.loader import load_pdf
from utils.ocr import is_scanned_pdf
from utils.splitter import split_documents
from utils.vectordb import create_vector_db
from utils.database import (
    add_document,
    document_exists
)
from utils.pdf_manager import (
    list_documents,
    delete_pdf
)
from utils.pdf_viewer import display_pdf


st.set_page_config(
    page_title="Documents",
    page_icon="📄"
)

st.title("📄 Document Manager")
st.caption("Upload, index and manage your PDF documents.")

# =====================================================
# Upload PDFs
# =====================================================

uploaded_files = st.file_uploader(
    "Upload PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    os.makedirs("pdfs", exist_ok=True)

    progress_bar = st.progress(0)

    status = st.empty()

    total_files = len(uploaded_files)

    for index, pdf in enumerate(uploaded_files):

        if document_exists(pdf.name):

            st.warning(f"⚠️ {pdf.name} is already indexed.")

            progress_bar.progress((index + 1) / total_files)

            continue

        pdf_path = os.path.join("pdfs", pdf.name)

        with open(pdf_path, "wb") as f:
            f.write(pdf.getbuffer())

        try:

            if is_scanned_pdf(pdf_path):

                status.info(
                    f"🖼️ {pdf.name} detected as a scanned PDF.\nRunning OCR..."
                )

            else:

                status.info(
                    f"📄 {pdf.name} detected as a digital PDF.\nExtracting text..."
                )

            with st.spinner(f"Processing {pdf.name}..."):

                docs, pages = load_pdf(pdf_path)

                chunks = split_documents(
                    docs,
                    pdf.name
                )

                create_vector_db(chunks)

                add_document(
                    filename=pdf.name,
                    pages=pages,
                    chunks=len(chunks)
                )

            st.success(
                f"✅ {pdf.name} indexed successfully "
                f"({pages} pages, {len(chunks)} chunks)"
            )

        except Exception as e:

            st.error(
                f"❌ Failed to process {pdf.name}\n\n{str(e)}"
            )

        progress_bar.progress((index + 1) / total_files)

    status.empty()

    st.success("🎉 All selected PDFs have been processed.")

# =====================================================
# Indexed Documents
# =====================================================

st.divider()

st.subheader("📚 Indexed Documents")

documents = list_documents()

if not documents:

    st.info("No indexed documents found.")

else:

    for filename, pages, chunks, upload_time in documents:

        with st.container(border=True):

            left, right = st.columns([5, 1])

            with left:

                st.markdown(f"### 📄 {filename}")

                c1, c2 = st.columns(2)

                c1.metric("Pages", pages)

                c2.metric("Chunks", chunks)

                st.caption(f"Uploaded: {upload_time}")

            with right:

                if st.button(
                    "👁 Preview",
                    key=f"preview_{filename}"
                ):

                    pdf_html = display_pdf(filename)

                    if pdf_html:

                        st.markdown(
                            pdf_html,
                            unsafe_allow_html=True
                        )

                    else:

                        st.error("PDF not found.")

                if st.button(
                    "🗑 Delete",
                    key=f"delete_{filename}"
                ):

                    with st.spinner("Deleting document..."):

                        delete_pdf(filename)

                    st.success(f"{filename} deleted successfully.")

                    st.rerun()