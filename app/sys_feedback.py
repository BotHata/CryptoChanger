from flask import request, render_template, redirect
from app import app

import sqlite3
import time


@app.route('/sys_feedback', methods=['POST'])
@app.route('/sys_feedback/', methods=['POST'])
def sys_feedback():
	form = request.form

	with sqlite3.connect('db/main.db') as db_public:
		try:
			cur = db_public.cursor()
			cur.execute("INSERT INTO support (mail, cont, time) VALUES ((?), (?), (?))", (form['mail'], form['cont'], time.time()))
			db_public.commit()

		except:
			db_public.rollback()
			# db_public.close()
			return render_template('message.html', cont='Ошибка!')

		else:
			# db_public.close()
			return redirect('/')