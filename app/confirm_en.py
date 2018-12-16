from flask import render_template
from app import app, LINK, get_reviews


@app.route('/confirm_en')
@app.route('/confirm_en/')
def confirm_en():
	return render_template('confirm_en.html',
		LINK = LINK,
		url = 'confirm_en',

		news = False,
		reviews = get_reviews(),
		message = None,
	)