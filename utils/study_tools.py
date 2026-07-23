from utils.chatbot import ask_gemini


def generate_summary(document=None, mode="executive"):
    """
    Generate different types of summaries.
    """

    prompts = {

        "executive": """
        Generate an executive summary.

        Include:
        - Objective
        - Problem
        - Method
        - Results
        - Conclusion

        Keep it under 300 words.
        """,

        "detailed": """
        Generate a detailed summary.

        Explain every important section.

        Use headings and paragraphs.
        """,

        "bullet": """
        Summarize the document using bullet points.

        Include only the most important facts.
        """,

        "takeaways": """
        Extract the 10 most important takeaways.

        Each takeaway should be one sentence.
        """,

        "minute": """
        Explain the document so someone can understand
        it in under one minute.
        """

    }

    answer, _ = ask_gemini(
        prompts[mode],
        document
    )

    return answer


def generate_notes(document=None):
    """
    Generate structured notes.
    """

    prompt = """
    Create well-structured study notes.

    Use headings, bullet points and important facts.
    """

    answer, _ = ask_gemini(
        prompt,
        document
    )

    return answer


def generate_flashcards(document=None):
    """
    Generate flashcards.
    """

    prompt = """
    Create 15 flashcards.

    Format:

    Q:
    A:

    Keep answers short.
    """

    answer, _ = ask_gemini(
        prompt,
        document
    )

    return answer


def generate_mcqs(document=None):

    prompt = """
Generate exactly 10 multiple-choice questions from the document.

Use ONLY this format.

Question: What is Machine Learning?

A) Option A

B) Option B

C) Option C

D) Option D

Answer: B

Explanation:
One short sentence explaining why the answer is correct.

-----------------------

Repeat for all questions.

Do not use markdown tables.

Do not use numbering.

Keep the format identical.
"""

    answer, _ = ask_gemini(prompt, document)

    return answer


def generate_interview_questions(document=None):
    """
    Generate interview questions.
    """

    prompt = """
    Generate technical interview questions
    from the document.

    Include answers.
    """

    answer, _ = ask_gemini(
        prompt,
        document
    )

    return answer