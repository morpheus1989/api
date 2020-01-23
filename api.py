from flask import Flask,request,session
from datetime import timedelta
import os
import config
app = Flask(__name__)
app.config.from_object(config)
# 加盐操作，随机数
app.config['SECRET_KEY']=os.urandom(24)
# 通过配置来修改session存储时间，2小时
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(hours=2)
@app.route('/')
def hello_world():
    # 设置session
    session['user']='杨过'
    # permanent，持久化；设置成true默认存储31天
    # 默认该参数为false，浏览器关闭失效
    session.permanent=True
    return 'hey boy!'

@app.route('/get/')
def get_session():
    user=session.get('user')
    return user or 'no find session'
@app.route('/del/')
def del_session():
    # pop不存在的键会有异常
    session.pop('user')
    # 删除所有session
    session.clear()
    return 'delete success'

if __name__ == '__main__':
    app.run()
