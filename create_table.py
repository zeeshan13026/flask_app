import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY,name text, price real)"
cursor.execute(create_table)

# insert_item = "INSERT INTO items VALUES('pen',20.5)"
# cursor.execute(insert_item)

connection.commit()
connection.close()