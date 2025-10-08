import sqlite3

conn = sqlite3.connect("database.db")

conn.executescript("""
CREATE TABLE IF NOT EXISTS posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  content TEXT NOT NULL
);
""")

conn.close()
print("✅ Tabla 'posts' creada correctamente.")