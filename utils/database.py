import sqlite3
from pathlib import Path

DB_PATH = Path("database/chat.db")


def get_connection():
    DB_PATH.parent.mkdir(exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)


def initialize_database():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT UNIQUE,
        pages INTEGER,
        chunks INTEGER,
        upload_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS chats (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        session_id INTEGER,

        question TEXT,

        answer TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(session_id)
            REFERENCES chat_sessions(id)
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS chat_sessions(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        session_name TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()

def add_document(filename, pages, chunks):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR REPLACE INTO documents
    (filename, pages, chunks)
    VALUES (?, ?, ?)
    """, (filename, pages, chunks))

    conn.commit()
    conn.close()


def get_documents():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT filename, pages, chunks, upload_time
    FROM documents
    ORDER BY upload_time DESC
    """)

    rows = cur.fetchall()

    conn.close()

    return rows

def save_chat(question, answer, document):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO chats
    (question, answer, document_name)
    VALUES (?, ?, ?)
    """, (question, answer, document))

    conn.commit()
    conn.close()


def get_chat_history():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT question, answer
    FROM chats
    ORDER BY id DESC
    """)

    rows = cur.fetchall()

    conn.close()

    return rows

def document_exists(filename):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT id FROM documents WHERE filename=?",
        (filename,)
    )

    exists = cur.fetchone() is not None

    conn.close()

    return exists

def delete_document(filename):
    """
    Delete a document record from SQLite.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM documents WHERE filename=?",
        (filename,)
    )

    conn.commit()
    conn.close()

def save_chat(session_id, question, answer):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO chats(
            session_id,
            question,
            answer
        )
        VALUES(?,?,?)
        """,
        (
            session_id,
            question,
            answer
        )
    )

    conn.commit()

    conn.close()


def get_chat_history(session_id):

    conn = get_connection()

    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            question,
            answer,
            created_at
        FROM chats
        WHERE session_id=?
        ORDER BY id ASC
        """,
        (session_id,)
    )

    rows = cur.fetchall()

    conn.close()

    return rows


def clear_chat_history(session_id):
    """
    Clear all messages for a specific chat session.
    """

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM chats
        WHERE session_id=?
        """,
        (session_id,)
    )

    conn.commit()
    conn.close()

def create_chat_session(name):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO chat_sessions(session_name)
        VALUES(?)
        """,
        (name,)
    )

    conn.commit()

    session_id = cur.lastrowid

    conn.close()

    return session_id


def get_chat_sessions():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, session_name
        FROM chat_sessions
        ORDER BY id DESC
        """
    )

    rows = cur.fetchall()

    conn.close()

    return rows


def delete_chat_session(session_id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM chats WHERE session_id=?",
        (session_id,)
    )

    cur.execute(
        "DELETE FROM chat_sessions WHERE id=?",
        (session_id,)
    )

    conn.commit()

    conn.close()