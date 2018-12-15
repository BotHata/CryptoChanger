# from app import app


from flask import Flask
from params import *

import sqlite3


app = Flask(__name__)
app.config.from_object('config')


# Получить отзывы
def get_reviews():
	with sqlite3.connect('db/main.db') as db:
		reviews = [{'id': i[0], 'name': i[1], 'cont': i[2]} for i in db.execute("SELECT * FROM reviews ORDER BY `id` DESC LIMIT 3")]

	return reviews

@app.route('/')
def index():
	referal = request.args.get('action')
	if not referal:
		referal = ''

	return render_template('index.html',
		LINK = LINK,
		url = '',

		news = True,
		reviews = get_reviews(),
		message = 'Перевод из RUB в BTC из-за большой нагрузки временно недоступен!',
		referal = referal,
	)



app.run(debug=True)