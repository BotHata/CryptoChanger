import sqlite3


db = sqlite3.connect('db/main.db')

for i in db.execute("SELECT * FROM history"):
	print(i)