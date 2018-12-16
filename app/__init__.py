from flask import Flask
from params import *

import sqlite3


app = Flask(__name__)
app.config.from_object('config')

# Получить отзывы
def get_reviews():
	with sqlite3.connect('db/main.db') as db:
		reviews = [{'id': i[0], 'name': i[1], 'cont': i[2]} for i in db.execute("SELECT * FROM reviews ORDER BY `id` DESC LIMIT 3")]

	return reviews


from app import index
from app import rules
from app import confirm
from app import en
from app import confirm_en

from app import sys_change_en
from app import sys_change
from app import sys_feedback
from app import sys_reviews