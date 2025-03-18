import sqlite3

class MemoryDB:
    def __init__(self, db_name="memory.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """CREATE TABLE IF NOT EXISTS interactions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        query TEXT UNIQUE, result TEXT)"""
        self.conn.execute(query)
        self.conn.commit()

    def store(self, query, result):
        self.conn.execute("INSERT OR REPLACE INTO interactions (query, result) VALUES (?, ?)", (query, result))
        self.conn.commit()

    def retrieve(self, query):
        cursor = self.conn.execute("SELECT result FROM interactions WHERE query=?", (query,))
        row = cursor.fetchone()
        return row[0] if row else None

