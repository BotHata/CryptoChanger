from flask import render_template
from app import app, LINK


@app.route('/confirm')
@app.route('/confirm/')
def confirm():
	return render_template('confirm.html',
		LINK = LINK,
		url = 'confirm',

		news = False,
	)