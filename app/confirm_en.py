from flask import render_template
from app import app, get_reviews


@app.route('/confirm_en')
@app.route('/confirm_en/')
def confirm_en():
	return render_template('confirm_en.html',
		url = 'confirm_en',

		news = False,
		reviews = get_reviews(),
		message = None,
	)