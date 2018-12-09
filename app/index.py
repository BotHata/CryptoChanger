from flask import render_template
from app import app, LINK, get_reviews


@app.route('/')
def index():
	return render_template('index.html',
		LINK = LINK,
		url = '',

		news = True,
		reviews = get_reviews(),
	)