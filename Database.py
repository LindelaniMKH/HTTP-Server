import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()
        self.drop = 'DROP TABLE IF EXIST users'
        self.cursor.execute(self.drop)

    def create_table(self):
        cursor = self.cursor

        query = '''
        CREATE TABLE IF NOT EXIST users(
            user_id PRIMARY KEY AUTOINCREMENT NOT NULL,
            user_name TEXT,
            user_surname TEXT,
            user_email TEXT UNIQUE
        )
        '''

        cursor.commit(query)
        cursor.close()
    
    def insert_table(self, name, surname, email):
        cursor = self.cursor

        query = 'INSERT INTO users (user_name, user_surname, user_email) VALUES (?, ?, ?)'

        cursor.commit(query, (name, surname, email))
        cursor.close()
