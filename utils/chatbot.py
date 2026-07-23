import google.generativeai as genai

from config import GOOGLE_API_KEY
from utils.vectordb import similarity_search
from utils.hybrid_search import hybrid_search
from utils.prompt_builder import build_prompt
from utils.citations import format_citations

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")


def ask_gemini(question, selected_document=None):
    """
    Search the vector database, generate an answer,
    and return both the answer and source citations.
    """

    # Retrieve relevant chunks
    docs = hybrid_search(
        query=question,
        selected_document=selected_document
    )

    prompt, citations = build_prompt(
        question,
        docs
    )

    if not docs:
        return (
            "I couldn't find any relevant information in the uploaded PDFs.",
            []
        )

    # Build context for Gemini
    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = f"""
You are an AI PDF Research Assistant.

Rules:
1. Answer ONLY using the provided context.
2. Do NOT make up information.
3. If the answer is not available, reply:
   "I couldn't find that information in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip()

    except Exception as e:
        answer = f"Gemini Error: {str(e)}"

    # Prepare source list
    sources = []

    for doc in docs:

        sources.append(
            {
                "file": doc.metadata.get("source", "Unknown"),
                "page": doc.metadata.get("page", 0) + 1
            }
        )

    # Remove duplicate sources
    unique_sources = []
    seen = set()

    for source in sources:

        key = (source["file"], source["page"])

        if key not in seen:
            seen.add(key)
            unique_sources.append(source)

    return (
        response.text,
        format_citations(citations)
    )