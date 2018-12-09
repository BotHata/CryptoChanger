from flask import request, render_template, redirect
from app import app, LINK

import sqlite3
import time


@app.route('/sys_change', methods=['POST'])
@app.route('/sys_change/', methods=['POST'])
def sys_change():
	form = request.form

	with sqlite3.connect('db/main.db') as db_public:
		try:
			cur = db_public.cursor()
			cur.execute("INSERT INTO history (name, mail, count, card, time) VALUES ((?), (?), (?), (?), (?))", (form['name'], form['mail'], float(form['count'].replace(',', '.')), form['card'], time.time()))
			db_public.commit()

		except:
			db_public.rollback()
			# db_public.close()
			return render_template('message.html', cont='Ошибка!')

		else:
			# db_public.close()
			return redirect(LINK + 'confirm/')