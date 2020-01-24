from flask import Flask,request,g,session
import config
app = Flask(__name__)
app.config.from_object(config)
@app.route('/')
def hello_world():
    if hasattr(g,'user'):
        print(g.user)
    return 'hello'

@app.route('/list/')
def list():
    session['user_id']=1
    return 'list'

# 第一次请求之前执行
# @app.before_first_request
# def first_request():
#     print('here is right')

# 钩子函数是使用特定的装饰器装饰的函数，形象地指将目标钩住
# 为何称为钩子函数？因为它可以在正常执行的代码中，插入一段自己想要执行的代码
# hook破解软件/操作系统
# 每次请求之前先执行，通常将后面多处用到的数据处理好，简化视图操作
@app.before_request
def before_req():
    user_id = session.get('user_id')
    if user_id:
        g.user='叶问'



if __name__ == '__main__':
    app.run()
