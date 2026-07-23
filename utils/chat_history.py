from utils.database import (
    save_chat,
    get_chat_history,
    clear_chat_history
)


def save_conversation(session_id, question, answer):

    save_chat(
        session_id,
        question,
        answer
    )


def load_conversations(session_id):

    return get_chat_history(session_id)


def delete_history(session_id):

    clear_chat_history(session_id)