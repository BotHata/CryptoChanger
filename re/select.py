import sqlite3


db = sqlite3.connect('db/main.db')

print('History')
for i in db.execute("SELECT * FROM history"):
	print(i)

print('Reviews')
for i in db.execute("SELECT * FROM reviews"):
	print(i)

print('Support')
for i in db.execute("SELECT * FROM support"):
	print(i)

print('News')
for i in db.execute("SELECT * FROM news"):
	print(i)