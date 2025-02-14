import sqlite3
from config import DATABASE_FILE_PATH
from config import DATABASE_FILE_PATH1
from config import DATABASE_FILE_PATH2

connection_bookref = sqlite3.connect(DATABASE_FILE_PATH)
connection_bookref.row_factory = sqlite3.Row

connection_aref = sqlite3.connect(DATABASE_FILE_PATH1)
connection_aref.row_factory = sqlite3.Row

connection_iref = sqlite3.connect(DATABASE_FILE_PATH2)
connection_iref.row_factory = sqlite3.Row

def get_bookref_connection():
    return connection_bookref

def get_aref_connection():
    return connection_aref

def get_iref_connection():
    return connection_iref
