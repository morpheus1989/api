from flask import Flask,request,g,render_template
import config

from flask import template_rendered,got_request_exception
from blinker import Namespace
# Namespace 命名空间；企业界别大项目，多人开发，避免同名信号冲突

# # 1 定义信号
# test_space=Namespace()
# # 放火信号
# fire_signal=test_space.signal('fire')
#
# # 2 监听信号，绑定回掉函数来处理该信号
# # 发射子弹
# def fire_bullet(sender,):
#     print(sender)
#     print('ready！fire bullet')
# fire_signal.connect(fire_bullet)
#
# # 3 发送信号
# fire_signal.send()

from signals import login_signal
app = Flask(__name__)
app.config.from_object(config)

def template_render_func(sender,template,context):
    # sender代表发送者，默认指当前app
    # template模版名；context模版可使用变量
    print(template,context)
template_rendered.connect(template_render_func)


# 上线后记录错误日志，不知道什么参数的时候可以使用*args,**kwargs来查看*ar
# def request_exception_log(sender,*args,**kwargs):
def request_exception_log(sender,exception):
    print(exception)
got_request_exception.connect(request_exception_log)

@app.route('/')
def hello():
    1/0
    return render_template('index.html')

@app.route('/login/')
def login():
    user=request.args.get('user')
    if user:
        g.user=user
        # 1 传参数
        # login_signal.send(user=user)
        # 2 绑定到g对象上
        login_signal.send()

        return 'ok login'
    else:
        return 'no login'

if __name__ == '__main__':
    app.run()
