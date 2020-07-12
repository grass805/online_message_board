'''
#1 step
initiate flask
IMPORTANT 檔名一定要__init__.py
'''

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy




app = Flask('flask_folder')  #consistent with flask folder name

app.config.from_pyfile('config.py') #import flask config settings

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

'''
一定要寫在最後面!!!!!!!
'''
from flask_folder import main, commands



