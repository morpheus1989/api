from flask import Flask, g, session, render_template,abort
import config

app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    # 使用abort主动抛出指定状态码的异常
    abort(500)
    if hasattr(g, 'user'):
        print(g.user)
    return render_template('index.html')


@app.route('/list/')
def list():
    session['user_id'] = 1
    return 'list'


# 第一次请求之前执行
# @app.before_first_request
# def first_request():
#     print('here is right')

# 钩子函数是使用特定的装饰器装饰的函数，形象地指将目标钩住
# 为何称为钩子函数？因为它可以在正常执行的代码中，插入一段自己想要执行的代码
# hook破解软件/操作系统
# 每次请求之前先执行，通常将后面多处用到的数据处理好，给视图函数添加一些变量，简化视图操作
# @app.before_request
# def before_req():
#     user_id = session.get('user_id')
#     if user_id:
#         setattr(g,'user','叶问')


# 不管是否有异常，注册函数都会在每次请求之后执行
# @app.teardown_appcontext
# def teardown(exc=None):
#     if exc is None:
#         db.session.commit()
#     else:
#         db.session.rollback()
#     db.session.remove()


# 自定义jinja模版过滤器
# @app.template_filter
# def upper_filter(s):
#     return s.upper()

# 上下文处理过滤器，返回字典中的键可以在模版上下文中使用
# 相当于所有模版的共享变量，省掉每个模版渲染时的公共变量传参；一处定义，多处使用
# 简洁的同时意味着好维护
# 必须返回字典
# @app.context_processor
# def context_process():
#     # 如果用户已经登录
#     if hasattr(g,'user'):
#         return {'current_user': '古龙'}
#     else:
#         return {}


# 山寨业余，不够美观；关掉debug模式，会触发服务器内部错误
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'),500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# 比如说用户不存在/网站未注册；user_id not find
@app.errorhandler(400)
def args_error(error):
    return render_template('400.html'), 400


if __name__ == '__main__':
    app.run()
