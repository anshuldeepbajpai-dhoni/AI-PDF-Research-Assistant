import re
import streamlit as st


# =====================================================
# Flashcards
# =====================================================

def render_flashcards(content):

    cards = re.findall(
        r"Q:(.*?)A:(.*?)(?=Q:|$)",
        content,
        flags=re.S
    )

    if not cards:
        st.markdown(content)
        return

    for i, (question, answer) in enumerate(cards):

        with st.expander(f"🧠 Flashcard {i+1}"):

            st.markdown(f"**Question**\n\n{question.strip()}")

            if st.button(
                "Reveal Answer",
                key=f"flash_{i}"
            ):
                st.success(answer.strip())


# =====================================================
# Interview Questions
# =====================================================

def render_interview(content):

    sections = re.findall(
        r"Q:(.*?)A:(.*?)(?=Q:|$)",
        content,
        flags=re.S
    )

    if not sections:
        st.markdown(content)
        return

    for q, a in sections:

        with st.expander(q.strip()):

            st.write(a.strip())


# =====================================================
# MCQ Quiz Engine
# =====================================================

def render_mcq(content):

    pattern = re.compile(

        r"Question:\s*(.*?)\n"
        r"A\)\s*(.*?)\n"
        r"B\)\s*(.*?)\n"
        r"C\)\s*(.*?)\n"
        r"D\)\s*(.*?)\n"
        r"Answer:\s*([ABCD])\n"
        r"Explanation:\s*(.*?)(?=\n-{5,}|$)",

        re.S

    )

    questions = pattern.findall(content)

    if not questions:

        st.error("Unable to parse MCQs.")

        st.markdown(content)

        return

    total = len(questions)

    # =====================================================
    # Session State
    # =====================================================

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    if "quiz_score" not in st.session_state:
        st.session_state.quiz_score = 0

    # =====================================================
    # Questions
    # =====================================================

    answers = []

    for i, q in enumerate(questions):

        question = q[0]

        options = {

            "A": q[1],

            "B": q[2],

            "C": q[3],

            "D": q[4]

        }

        correct = q[5]

        explanation = q[6].strip()

        st.markdown(f"## Question {i+1}")

        st.write(question)

        selected = st.radio(

            "Choose an answer",

            list(options.keys()),

            format_func=lambda x: f"{x}) {options[x]}",

            key=f"answer_{i}",

            disabled=st.session_state.quiz_submitted

        )

        answers.append(
            (
                selected,
                correct,
                options,
                explanation
            )
        )

        st.divider()

    # =====================================================
    # Submit Quiz
    # =====================================================

    if not st.session_state.quiz_submitted:

        if st.button(
            "✅ Submit Quiz",
            use_container_width=True
        ):

            score = 0

            st.session_state.quiz_submitted = True

            for selected, correct, _, _ in answers:

                if selected == correct:
                    score += 1

            st.session_state.quiz_score = score

            st.rerun()

    # =====================================================
    # Results
    # =====================================================

    if st.session_state.quiz_submitted:

        score = st.session_state.quiz_score

        percentage = round(
            score / total * 100,
            1
        )

        st.success(
            f"Final Score: {score}/{total}"
        )

        st.metric(
            "Percentage",
            f"{percentage}%"
        )

        st.progress(score / total)

        if percentage >= 90:

            st.success("🏆 Excellent")

        elif percentage >= 75:

            st.success("🎉 Good Job")

        elif percentage >= 50:

            st.warning("🙂 Fair")

        else:

            st.error("📚 Needs More Practice")

        st.divider()

        st.subheader("Review Answers")

        for i, q in enumerate(questions):

            selected, correct, options, explanation = answers[i]

            with st.expander(
                f"Question {i+1}"
            ):

                st.write(q[0])

                st.write(
                    f"**Your Answer:** {selected}) {options[selected]}"
                )

                st.write(
                    f"**Correct Answer:** {correct}) {options[correct]}"
                )

                st.info(explanation)

        if st.button(
            "🔄 Restart Quiz",
            use_container_width=True
        ):

            st.session_state.quiz_submitted = False

            st.session_state.quiz_score = 0

            for i in range(total):

                key = f"answer_{i}"

                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()