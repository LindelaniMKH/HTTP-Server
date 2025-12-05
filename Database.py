import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('users.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.drop = 'DROP TABLE IF EXISTS users'
        self.cursor.execute(self.drop)
        self.conn.commit()

    def create_table(self):
        cursor = self.cursor
        conn = self.conn

        query = '''
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_name TEXT,
            user_surname TEXT,
            user_email TEXT UNIQUE
        )
        '''

        cursor.execute(query)
        conn.commit()
    
    def insert_table(self, name, surname, email):
        cursor = self.cursor
        conn = self.conn

        query = 'INSERT INTO users (user_name, user_surname, user_email) VALUES (?, ?, ?)'

        cursor.execute(query, (name, surname, email))
        conn.commit()
        conn.close()
