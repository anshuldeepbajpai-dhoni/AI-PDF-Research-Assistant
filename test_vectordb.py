from utils.loader import load_pdf
from utils.splitter import split_documents
from utils.vectordb import create_vector_db

docs = load_pdf("pdfs/sample.pdf")

chunks = split_documents(docs)

db = create_vector_db(chunks)

print("Database Created Successfully")

print("Number of Chunks:", db._collection.count())