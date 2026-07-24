from utils.loader import load_pdf
from utils.splitter import split_documents

docs = load_pdf("pdfs/sample.pdf")

print("Pages:", len(docs))

chunks = split_documents(docs)

print("Chunks:", len(chunks))