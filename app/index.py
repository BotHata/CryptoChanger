from flask import render_template, request
from app import app, LINK, get_reviews


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
		referal = referal,
	)