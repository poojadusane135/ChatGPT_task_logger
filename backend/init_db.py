import sqlite3

conn = sqlite3.connect("chats.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS chat_logs(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    timestamp TEXT,

    title TEXT,

    content TEXT,

    source TEXT

)
""")

conn.commit()

conn.close()

print("Database Created")