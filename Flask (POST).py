from flask import Flask
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def create_connection(path):
    connection = None
    try:
        connection  = sqlite3.connect(path)
        print("Connection to SQLite DB Succesful")
    except Error as e:
        print(f"The error '{e}' occured")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed succesfully")
    except Error as e:
        print(f"The error '{e}' occured")

    return cursor

@app.route('/', methods = ['POST'])
def table():
    connection = create_connection("SQLite")
    query = """
CREATE TABLE Chat
(id INT PRIMARY KEY,
nama TEXT,
pesan TEXT);
"""
    connection.cursor().execute(query)
    connection.commit()

    return "DB Created Succesfully"

@app.route('/insert', methods = ['POST'])
def insert():
    connection = create_connection("SQLite")
    body = request.json
    query = f"""
INSERT INTO chat (name, message)
VALUES ("{body['name']}", "{body['message']}")
"""
    execute_query(connection, query)
    return {"status": 200}

app.run(host='0.0.0.0', port=3000)
