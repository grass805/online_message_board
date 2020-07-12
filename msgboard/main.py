'''
#5 step
main function
'''

from flask import flash, redirect, url_for, render_template

from flask_folder import app, db
from flask_folder.model import Message
from flask_folder.forums import submitForum

@app.route('/', methods=['GET', 'POST']) 
#在https://app.route/ 頁面，GET: 接收使用者的輸入，接著POST回傳訊息給使用者

def index():
    # initdb();
    form = submitForum()
    if form.validate_on_submit():  #如果表單驗證為True
        name = form.name.data
        body = form.body.data
        message = Message(body=body, name=name)
        db.session.add(message)  #db.session.add(資料)可以將資料加入產生新增資料的SQL語法
        db.session.commit()   #db.session.commit()可以執行指令
        flash('message sent')  #feedback message displayed to user
        return redirect(url_for('index')) #url_for('def函數的字串形式')，會回傳'位置'  @app.route('位置')
                                            #跳轉到redirect(指定的url)
    messages2 = Message.query.order_by(Message.timestamp.desc()).all() #query.order_by():數據按什麼方式排序，timestamp.desc():時間大到小
    return render_template('index.html', form=form, messages=messages2)#將參數傳入前端 html template，(在templates資料夾下要套用模板的html檔，後面設定要html參數傳入值)
    
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=80)

