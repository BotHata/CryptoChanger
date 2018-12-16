from flask import render_template
from app import app, get_reviews


@app.route('/rules')
@app.route('/rules/')
def rules():
	return render_template('sosaka.html',
		url = 'rules',

		news = False,
		reviews = get_reviews(),
		message = None,
	)