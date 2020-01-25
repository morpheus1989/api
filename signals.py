# 定义一个登录的信号，以后用户登录进来就发送一个登录信号
# 监听到后就记录当前用户登录的信息；用信号方式，记录用户的登录信息

from blinker import Namespace
from datetime import datetime
from flask import request,g
namespace=Namespace()
login_signal=namespace.signal('login')

"""
模版渲染后
template_rendered=1
模版渲染前
before_render_template = 2
请求开始/结束/对象销毁时
request_started =3
request_finished = 4
request_tearing_down = 5
视图函数发生异常；监听信号，查找bug
got_request_exception = 6
app上下文被销毁时
appcontext_tearing_down =7
app上下文入栈/出栈
appcontext_pushed = 8
appcontext_popped = 9
从flask中给模版发送信息，不常用
message_flashed = 10

依葫芦画瓢
"""
# 信号：模版已被渲染/
from flask import template_rendered

# def login_log(sender,user):
def login_log(sender):
    # 监听到信号，存储什么信息以及应该怎么存储
    # 用户名/登录时间/ip地址/
    print(sender)
    now=datetime.now()
    # 获取用户访问ip，request属于全局变量
    ip=request.remote_addr
    user=g.user
    log_msg='{}*{}*{}'.format(user,now,ip)
    print('用户已经登录')
    # window写文件权限不允许，以管理员权限打开cmd，然后执行主文件，运行app
    with open('log.txt','a+') as f:
        f.write(log_msg+'\n')


login_signal.connect(login_log)