from flask import Flask,url_for
import config

from flask_restful import Api,Resource
app = Flask(__name__)
app.config.from_object(config)

# 使用Api绑定app，返回api对象
api=Api(app)

class LoginView(Resource):
    # def post(self):
    #     return 'post ok'
    def post(self,user=None):
        return dict(user=user)

api.add_resource(LoginView,'/login/<user>/','/regist/')

with app.test_request_context():
    # print(url_for('login'))
    print(url_for('loginview',user='hero'))

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
