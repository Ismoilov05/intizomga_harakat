import sqlite3

def get_connection():
    conn = sqlite3.connect("discipline.db")
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        focus_score INTEGER,
        comment TEXT
    )''')
    conn.commit()
    conn.close()

def add_report(user_id, date, focus_score, comment):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO reports (user_id, date, focus_score, comment) VALUES (?, ?, ?, ?)",
                (user_id, date, focus_score, comment))
    conn.commit()
    conn.close()
