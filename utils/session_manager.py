import streamlit as st

from utils.database import (
    create_chat_session,
    get_chat_sessions,
    delete_chat_session
)


def initialize_session():

    if "current_session" not in st.session_state:

        sessions = get_chat_sessions()

        if sessions:

            st.session_state.current_session = sessions[0][0]

        else:

            session_id = create_chat_session("Chat 1")

            st.session_state.current_session = session_id


def get_current_session():

    return st.session_state.current_session


def create_new_session():

    sessions = get_chat_sessions()

    name = f"Chat {len(sessions)+1}"

    session_id = create_chat_session(name)

    st.session_state.current_session = session_id

    return session_id


def switch_session(session_id):

    st.session_state.current_session = session_id


def remove_session(session_id):

    delete_chat_session(session_id)

    sessions = get_chat_sessions()

    if sessions:

        st.session_state.current_session = sessions[0][0]

    else:

        new_id = create_chat_session("Chat 1")

        st.session_state.current_session = new_id