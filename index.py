from flask import Flask, render_template, request
# from pymongo import MongoClient

# import sqlite3
import time
import json


app = Flask(__name__)

# # Получить отзывы
# def get_reviews():
# 	with sqlite3.connect('db/main.db') as db:
# 		reviews = [{'id': i[0], 'name': i[1], 'cont': i[2]} for i in db.execute("SELECT * FROM reviews ORDER BY `id` DESC LIMIT 3")]

# 	return reviews


@app.route('/')
def index():
	referal = request.args.get('action')
	if not referal:
		referal = ''

	return render_template('index.html',
		url = '',

		news = True,
		reviews = [], # get_reviews(),
		message = 'Перевод из RUB в BTC из-за большой нагрузки временно недоступен!',
		referal = referal,
	)

@app.route('/rules')
@app.route('/rules/')
def rules():
	return render_template('rules.html',
		url = 'rules',

		news = False,
		reviews = [], # get_reviews(),
		message = None,
	)

@app.route('/confirm')
@app.route('/confirm/')
def confirm():
	return render_template('confirm.html',
		url = 'confirm',

		news = False,
		reviews = [], # get_reviews(),
		message = None,
	)


@app.route('/sys_change', methods=['POST'])
@app.route('/sys_change/', methods=['POST'])
def sys_change():
	# form = request.form
	# course = request.args.get('cur')
	# course = float(course) if course else 0.0
	# referal = request.args.get('ref')
	# if not referal:
	# 	referal = ''

	# cur = db_public.cursor()
	# cur.execute("INSERT INTO history (name, mail, count, card, course, referal, time) VALUES ((?), (?), (?), (?), (?), (?), (?))", (form['name'], form['mail'], float(form['count'].replace(',', '.')), form['card'], course, referal, time.time()))
	# db_public.commit()

	# req = {
	# 	'name': form['name'],
	# 	'mail': form['mail'],
	# 	'count': float(form['count'].replace(',', '.')),
	# 	'card': form['card'],
	# 	'course': course,
	# 	'referal': referal,
	# 	'time': time.time(),
	# }

	# with open('db/re.db', 'a') as file:
	# 	print(json.dumps(req), file=file)

	return '<script>document.location.href = "/confirm/"</script>'


if __name__ == '__main__':
	app.run(debug=True)