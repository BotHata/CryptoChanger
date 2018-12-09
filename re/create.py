import sqlite3


db = sqlite3.connect('db/main.db')

db.execute("CREATE TABLE history (id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(100), mail varchar(100), count real, card varchar(50), time timestamp)")
db.execute("CREATE TABLE support (id INTEGER PRIMARY KEY AUTOINCREMENT, mail varchar(100), cont text, time timestamp)")
db.execute("CREATE TABLE reviews (id INTEGER PRIMARY KEY, name varchar(100), cont text, time timestamp)")
db.execute("CREATE TABLE news (id INTEGER PRIMARY KEY AUTOINCREMENT, cont text, time timestamp)")