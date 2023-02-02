from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

    return cursor

@app.route('/', methods = ['GET'])
def table():
    connection = create_connection("SQLite")
    query = """
CREATE TABLE
siswa (nama TEXT PRIMARY KEY,
kelas TEXT,
nilai INT);
"""
    connection.cursor().execute(query)
    connection.commit()

    return "DB Created Successfully"

@app.route('/insert', methods = ['GET'])
def insert():
    connection = create_connection("SQLite")
    query = """
INSERT INTO
nama ("nama") : VALUES ("Strring");
kelas ("kelas") : VALUES ("String");
nilai ("nilai") : VALUES (100)
"""
    execute_query(connection, query)

    return "DB Inserted Successfully"

app.run(host='0.0.0.0', port=3000)

