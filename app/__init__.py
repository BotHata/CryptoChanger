from flask import Flask
from params import *


app = Flask(__name__)
app.config.from_object('config')

# # Сформировать абсолютную ссылку
# def get_url(url, rep='competions'):
# 	if not url: url = rep
# 	if url == 'index': url = ''
# 	return redirect(LINK_CLIENT + url)


from app import index
from app import rules