import os
import sqlite3

class Db():
    def __init__(self):
        DB_DIR = os.getenv('DB_DIR', '/var/lib/remote')
        self.conn = sqlite3.connect('{}/remote.db'.format(DB_DIR))

    def initdb(self):
        schema = '''CREATE TABLE IF NOT EXISTS movie (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            path TEXT NOT NULL,
            overview TEXT NOT NULL,
            genre TEXT NOT NULL,
            poster_url TEXT NOT NULL
            );'''
        c = self.conn.cursor()
        c.execute(schema)
        self.conn.commit()

    def insert(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def delete(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        self.conn.commit()

    def query(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        data = c.fetchall()
        self.conn.commit()
        return data
