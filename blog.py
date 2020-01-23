from flask import Blueprint, request

blog_bp = Blueprint('blog', __name__, subdomain='blog')


@blog_bp.route('/')
def index():
    # request.args/form/files/
    user = request.cookies.get('user')
    # 三目运算符连接字 or/and
    return user or 'no find cookie'
