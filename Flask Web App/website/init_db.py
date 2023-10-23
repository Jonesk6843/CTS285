import sqlite3

connection = sqlite3.connect('userDatabase.db')
with open('schema.sql') as f:
        connection.executescript(f.read())
cur = connection.cursor()

cur.execute("INSERT INTO users (id#, firstname, email, userPass), VALUES (?, ?, ?, ?)")
connection.commit()
connection.close()