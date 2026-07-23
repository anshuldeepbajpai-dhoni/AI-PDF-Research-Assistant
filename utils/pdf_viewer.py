import os
import base64

PDF_FOLDER = "pdfs"


def display_pdf(filename):
    """
    Display a PDF inside Streamlit.
    """

    pdf_path = os.path.join(PDF_FOLDER, filename)

    if not os.path.exists(pdf_path):
        return None

    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{base64_pdf}"
        width="100%"
        height="700"
        type="application/pdf">
    </iframe>
    """

    return pdf_display