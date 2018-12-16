from flask import render_template
from app import app, get_reviews


@app.route('/confirm')
@app.route('/confirm/')
def confirm():
	return render_template('confirm.html',
		url = 'confirm',

		news = False,
		reviews = get_reviews(),
		message = None,
	)