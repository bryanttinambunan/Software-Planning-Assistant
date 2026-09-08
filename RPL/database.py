import sqlite3

conn = sqlite3.connect("tasks.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    assigned_to TEXT,
    priority TEXT,
    deadline TEXT,
    status TEXT
)
""")

conn.commit()