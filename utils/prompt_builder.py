from datetime import datetime


def build_prompt(question, documents):
    """
    Build a structured prompt for Gemini.
    """

    context = []

    citations = []

    for i, doc in enumerate(documents, start=1):

        source = doc.metadata.get("source", "Unknown")

        page = doc.metadata.get("page", "Unknown")

        chunk = doc.metadata.get("chunk_id", "Unknown")

        context.append(
            f"""
Document {i}

Source : {source}

Page   : {page}

Chunk  : {chunk}

Content:
{doc.page_content}
"""
        )

        citations.append(
            {
                "source": source,
                "page": page,
                "chunk": chunk
            }
        )

    prompt = f"""
You are an AI Research Assistant.

Use ONLY the provided context to answer.

If the answer is not present in the context, say:

"I couldn't find enough information in the uploaded documents."

Never hallucinate.

Always answer clearly using markdown.

==========================
QUESTION
==========================

{question}

==========================
CONTEXT
==========================

{"".join(context)}
"""

    return prompt, citations