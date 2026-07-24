from sentence_transformers import SentenceTransformer

print("Import Successful")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

print("Model Loaded Successfully")

embedding = model.encode("Hello World")

print(embedding.shape)