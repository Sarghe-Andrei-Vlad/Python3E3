import sqlite3

conn = sqlite3.connect('MyNotesDatabase.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        text TEXT
    )
""")

conn.commit()
conn.close()