import sqlite3

class Database:
    def __init__(self):
    # Create DB and Table Workers

        self.conn = sqlite3.connect('app.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS workers (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        hours REAL NOT NULL,
                        value_hours REAL NOT NULL,
                        worked_days INTEGER NOT NULL,
                        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        self.conn.commit()


    def insert_worker(self, worker):
    # Insert worker in database
        self.cur.execute('''INSERT INTO workers (name, hours, value_hours, worked_days)
                VALUES (?, ?, ?, ?)''', (worker[0], worker[1], worker[2], worker[3]))
        self.conn.commit()

    def search_worker_by_id(self, id):
        self.workerq = self.cur.execute('''SELECT * FROM workers WHERE id = ?''', (id))
        
