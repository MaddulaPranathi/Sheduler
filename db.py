import sqlite3

def init_db():
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reminders
                 (id INTEGER PRIMARY KEY, task TEXT, datetime TEXT)''')
    conn.commit()
    conn.close()

def add_reminder(task, datetime):
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute("INSERT INTO reminders (task, datetime) VALUES (?, ?)", (task, datetime))
    conn.commit()
    conn.close()
