import sqlite3


db = sqlite3.connect('db/main.db')

db.execute("CREATE TABLE history (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(100), mail varchar(100), count real, card varchar(50), time timestamp)")