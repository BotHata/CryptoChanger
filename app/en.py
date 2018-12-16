from flask import render_template
from app import app, LINK, get_reviews


@app.route('/en')
@app.route('/en/')
def en():
	return render_template('index_en.html',
		LINK = LINK,
		url = 'en',

		news = False,
		reviews = get_reviews(),
		message = 'USD to Bitcoin exchange are temporarily unavailable!',
	)