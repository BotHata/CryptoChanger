from flask import Flask, render_template, request
from pymongo import MongoClient

import time
import json


app = Flask(__name__)
db = MongoClient('mongodb://root:asdrqwerty09@invo-shard-00-00-guyjh.mongodb.net:27017,invo-shard-00-01-guyjh.mongodb.net:27017,invo-shard-00-02-guyjh.mongodb.net:27017/INVO?ssl=true&replicaSet=INVO-shard-0&authSource=admin')['exchanger']

# Получить отзывы

def get_reviews():
	return [i for i in db['reviews'].find({}, {'_id': False, 'time': False})][-3:][::-1]


@app.route('/')
def index():
	referal = request.args.get('action')
	if not referal:
		referal = ''

	return render_template('index.html',
		url = '',

		news = True,
		reviews = get_reviews(),
		message = 'Перевод из RUB в BTC из-за большой нагрузки временно недоступен!',
		referal = referal,
	)

@app.route('/rules')
@app.route('/rules/')
def rules():
	return render_template('rules.html',
		url = 'rules',

		news = False,
		reviews = get_reviews(),
		message = None,
	)

@app.route('/confirm')
@app.route('/confirm/')
def confirm():
	return render_template('confirm.html',
		url = 'confirm',

		news = False,
		reviews = get_reviews(),
		message = None,
	)


@app.route('/sys_change')
@app.route('/sys_change/')
def sys_change():
	course = request.args.get('cur')
	course = float(course) if course else 0.0

	referal = request.args.get('ref')
	if not referal:
		referal = ''

	req = {
		'name': request.args.get('name'),
		'mail': request.args.get('mail'),
		'count': float(request.args.get('count').replace(',', '.')),
		'card': request.args.get('card'),
		'course': course,
		'referal': referal,
		'time': time.time(),
	}

	db['history'].insert_one(req)

	return '<script>document.location.href = "/confirm/"</script>'


if __name__ == '__main__':
	app.run(debug=True)