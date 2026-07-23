import google.generativeai as genai

from config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-flash-latest")


def ask_gemini(question, context):

    prompt = f"""
You are an AI PDF Research Assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, reply:

"I couldn't find that information in the uploaded PDF."

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text