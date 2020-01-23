from flask import Flask, render_template, views, request
import config
from forms import RegistForm
from exts import db
from models import User

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


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

app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))

if __name__ == '__main__':
    app.run()
