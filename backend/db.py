import sqlite3
import json

DB = "storage/docs.db"


def get_conn():
    return sqlite3.connect(DB)


def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS chunks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pdf_id TEXT,
        page INTEGER,
        text TEXT,
        embedding TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS chats (
        session_id TEXT PRIMARY KEY,
        pdf_id TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        session_id TEXT,
        role TEXT,
        text TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_chunk(pdf_id, page, text, embedding):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "INSERT INTO chunks (pdf_id, page, text, embedding) VALUES (?, ?, ?, ?)",
        (pdf_id, page, text, json.dumps(embedding))
    )

    conn.commit()
    conn.close()


def get_chunks(pdf_id):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "SELECT page, text, embedding FROM chunks WHERE pdf_id=?",
        (pdf_id,)
    )

    rows = c.fetchall()
    conn.close()

    return rows


def create_session(session_id, pdf_id):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "INSERT INTO chats (session_id, pdf_id) VALUES (?, ?)",
        (session_id, pdf_id)
    )

    conn.commit()
    conn.close()


def get_session(session_id):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "SELECT pdf_id FROM chats WHERE session_id=?",
        (session_id,)
    )

    row = c.fetchone()
    conn.close()

    return row[0] if row else None


def add_message(session_id, role, text):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "INSERT INTO messages (session_id, role, text) VALUES (?, ?, ?)",
        (session_id, role, text)
    )

    conn.commit()
    conn.close()


def get_history(session_id):
    conn = get_conn()
    c = conn.cursor()

    c.execute(
        "SELECT role, text FROM messages WHERE session_id=?",
        (session_id,)
    )

    rows = c.fetchall()
    conn.close()

    return [{"role": r, "text": t} for r, t in rows]
