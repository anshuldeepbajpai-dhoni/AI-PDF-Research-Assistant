import numpy as np
from pathlib import Path

import easyocr
import fitz
from langchain_core.documents import Document

# Initialize EasyOCR only once
reader = easyocr.Reader(
    ["en"],
    gpu=False
)


def is_scanned_pdf(pdf_path):
    """
    Returns True if the PDF appears to be scanned,
    otherwise False.
    """

    document = fitz.open(pdf_path)

    pages_to_check = min(3, len(document))

    for i in range(pages_to_check):

        page = document.load_page(i)

        text = page.get_text().strip()

        if len(text) > 50:
            document.close()
            return False

    document.close()

    return True

def extract_text_from_scanned_pdf(pdf_path):
    """
    Extract scanned PDF page-by-page using EasyOCR.

    Returns:
        list[Document]
    """

    pdf_name = Path(pdf_path).name

    document = fitz.open(pdf_path)

    docs = []

    for page_number in range(len(document)):

        page = document.load_page(page_number)

        pix = page.get_pixmap(dpi=300)

        image = np.frombuffer(
            pix.samples,
            dtype=np.uint8
        ).reshape(
            pix.height,
            pix.width,
            pix.n
        )

        text = "\n".join(

            reader.readtext(
                image,
                detail=0,
                paragraph=True
            )

        )

        docs.append(

            Document(

                page_content=text,

                metadata={
                    "source": pdf_name,
                    "page": page_number + 1,
                    "ocr": True
                }

            )

        )

    document.close()

    return docs