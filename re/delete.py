import sqlite3


db = sqlite3.connect('db/main.db')

with db:
	db.execute("DELETE FROM reviews WHERE id=(?)'", (0,))