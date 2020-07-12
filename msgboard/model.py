'''
#3 step
SQLAlchemy database model   for messages
'''

from datetime import datetime
from flask_folder import db
#in _init_.py: db = SQLAlchemy(app)

class Message(db.Model):    # db.Model 一定要寫正確
    id = db.Column(db.Integer, primary_key=True) #設定為主鍵
    name = db.Column(db.String(20))  #字符串(最大长度) 使用者名稱最長20
    body = db.Column(db.String(100)) #留言長度最2多100
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True) #index = True (建立索引值)
    
    
    # def initdb():   #初始化數據庫
    #     db.create_all()
    
    