from sql import public, private


with public:
	public.execute("CREATE TABLE main (name varchar(100), cont text, time timestamp)")

with private:
	private.execute("CREATE TABLE main (name varchar(100), cont text)")
	private.execute("CREATE TABLE notes (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cont text, time timestamp, category int, tags text)")