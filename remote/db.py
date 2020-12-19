import os
import sqlite3

class Db():
    def __init__(self):
        DB_DIR = os.getenv('DB_DIR', '/var/lib/remote')
        self.conn = sqlite3.connect('{}/remote.db'.format(DB_DIR))
        self._initdb()

    def _initdb(self):
        schema = '''CREATE TABLE IF NOT EXISTS movie2 (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            year TEXT NOT NULL,
            overview TEXT NOT NULL,
            filename TEXT NOT NULL,
            poster_url TEXT NOT NULL
            );'''
        c = self.conn.cursor()
        c.execute(schema)
        self.conn.commit()

    def insert(self, sql, *values):
        c = self.conn.cursor()
        c.executemany(sql, [values])
        self.conn.commit()

    def delete(self, sql, *values):
        c = self.conn.cursor()
        c.executemany(sql, [values])
        self.conn.commit()

    def query(self, sql):
        c = self.conn.cursor()
        c.execute(sql)
        data = c.fetchall()
        self.conn.commit()
        return data
