from flask import render_template, request
from app import app, LINK


@app.route('/')
def index():
	return render_template('index.html',
		LINK = LINK,
		url = '',
	)