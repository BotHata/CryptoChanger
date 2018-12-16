from flask import request, render_template, redirect
from app import app

import sqlite3
import time


@app.route('/sys_change_en', methods=['POST'])
@app.route('/sys_change_en/', methods=['POST'])
def sys_change_en():
	form = request.form
	course = request.args.get('cur')
	course = float(course) if course else 0.0
	referal = request.args.get('ref')
	if not referal:
		referal = ''

	with sqlite3.connect('db/main.db') as db_public:
		try:
			cur = db_public.cursor()
			cur.execute("INSERT INTO history (name, mail, count, card, course, referal, time) VALUES ((?), (?), (?), (?), (?), (?), (?))", (form['name'], form['mail'], float(form['count'].replace(',', '.')), form['card'], course, referal, time.time()))
			db_public.commit()

		except:
			db_public.rollback()
			# db_public.close()
			return render_template('message.html', cont='Error!')

		else:
			# db_public.close()
			return redirect('/confirm_en/')
		