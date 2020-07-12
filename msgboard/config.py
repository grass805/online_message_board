'''
#2 step
configuration settings
'''

import os
import sys

from flask_folder import app
#in _init_.py: app = Flask('flask_folder')


#the SQLite URL address format is different on Linux/Mac and Windows systems
if sys.platform.startswith('win'):   #for Windows system
    prefix = 'sqlite:///'
else:                               #for Linux/Mac
    prefix = 'sqlite:////'
    

db_uri = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

#Flask-SQLAlchemy有自己的事件通知系统，需要额外的资源 --> 如不需要，關閉他可省資源
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', db_uri)
#Flask使用SECRET_KEY密钥来对cookies和别的东西进行签名，考虑到安全性, 密钥不建议存储在程序中. 最好存储在系统环境变量中, 通过 os.getenv(key, default=None) 获得
SECRET_KEY =os.getenv('SECRET_KEY', 'secret string')

