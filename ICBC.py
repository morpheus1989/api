from flask import Flask, render_template, views, request, session
import config
from forms import RegistForm, LoginForm, TransferForm
from exts import db
from models import User
from auth import login_required

# CsrfProtect是老版本
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# 绑定app，开启保护，防御攻击
# app.jinja_env.globals['csrf_token'] = generate_csrf jinja中已存在该环境变量--方法
CSRFProtect(app)

@app.route('/')
def index():
    return render_template('index.html')


class RegistView(views.MethodView):

    def get(self):
        return render_template('regist.html')

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            user = form.user.data
            pwd = form.pwd.data
            deposit = form.deposit.data
            user = User(user=user, email=email, pwd=pwd, deposit=deposit)
            db.session.add(user)
            db.session.commit()
            return '注册成功'

        else:
            print(form.errors)
            return '注册失败'


class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            pwd = form.pwd.data
            user = User.query.filter(User.email == email, User.pwd == pwd).first()
            if user:
                session['user_id'] = user.id
                return '登录成功'
            else:
                return '邮箱或者密码错误'

        return '邮箱或者密码错误'


class TransferView(views.MethodView):
    decorators=[login_required]
    def get(self):
        return render_template('transfer.html')

    def post(self):
        form = TransferForm(request.form)
        if form.validate():
            email = form.email.data
            money = form.money.data
            user = User.query.filter_by(email=email).first()
            if user:
                user_id = session.get('user_id')
                print(user_id)
                myself = User.query.get(user_id)
                if myself.deposit >= money:
                    user.deposit += money
                    myself.deposit -= money
                    db.session.commit()
                    return '转账成功'
                else:
                    return '余额不足'
            else:
                return '用户不存在'

        return '邮箱或者金额错误'


app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/transfer/', view_func=TransferView.as_view('transfer'))

if __name__ == '__main__':
    app.run()
