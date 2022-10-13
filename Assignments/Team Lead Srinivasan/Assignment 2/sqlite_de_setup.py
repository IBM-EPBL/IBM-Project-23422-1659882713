import sqlite3

conn = sqlite3.connect('students.db')
print("opened data base successfully")

conn.execute('CREATE TABLE user1 (email TEXT, password TEXT, address TEXT, city TEXT, state TEXT, zip TEXT)')

print("Table created")
conn.close()