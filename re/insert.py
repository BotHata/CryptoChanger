from sql import public, private
import time


with public:
	public.execute("INSERT INTO main (name, cont, time) VALUES ('portfolio', '', (?))", (time.time(),))