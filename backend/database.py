import sqlite3
from datetime import datetime


DB_NAME = "chats.db"


def save_chat(timestamp, title, content):

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO chat_logs
        (
            timestamp,
            title,
            content,
            source
        )
        VALUES
        (
            ?,?,?,?
        )
        """,
        (
            timestamp,
            title,
            content,
            "chatgpt"
        )
    )

    conn.commit()

    conn.close()


def get_today_chats():

    today = datetime.now().strftime("%Y-%m-%d")

    conn = sqlite3.connect(DB_NAME)

    cur = conn.cursor()

    cur.execute(
        """
        SELECT *
        FROM chat_logs
        WHERE DATE(timestamp) = ?
        ORDER BY id DESC
        """,
        (today,)
    )

    rows = cur.fetchall()

    conn.close()

    return rows
