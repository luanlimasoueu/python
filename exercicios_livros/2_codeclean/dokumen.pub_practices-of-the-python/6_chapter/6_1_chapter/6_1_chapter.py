import sqlite3
class DatabaseManager:
    def __init__(self, database_filename):
        self.connection = sqlite3.connect(database_filename)
    
    def _execute(self, statement):
        self.connection = sqlite3.connect(self.database_filename)
        cursor = self.connection.cursor()
        cursor.execute(statement)
        return cursor

statement = """CREATE TABLE IF NOT EXISTS bookmarks
(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL,
notes TEXT,
date_added TEXT NOT NULL
);"""
DatabaseManager('loja')
DatabaseManager('loja')._execute(statement)