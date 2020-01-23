from flask import redirect,url_for,session
from functools import wraps


def login_required(func):
    # 不使用wrap装饰器包裹有可能会丢失签名信息/自己名字
    @wraps(func)
    def wrapper(*args,**kwargs):
        user_id =session.get('user_id')
        if user_id:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper