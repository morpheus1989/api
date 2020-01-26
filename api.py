from flask import Flask,url_for
import config

from flask_restful import Api,Resource,reqparse,inputs
app = Flask(__name__)
app.config.from_object(config)

api=Api(app)

class LoginView(Resource):
    def post(self):
        # 参数验证对象
        parser=reqparse.RequestParser()
        # 字段名/转换类型/默认值/是否必须/choices/help错误提示信息/trim是否要去掉前后的空格
        parser.add_argument('user',type=str,help='用户验证失败',required=True)
        parser.add_argument('pwd',type=str,help='密码验证失败')
        parser.add_argument('age',type=int,help='年龄验证失败',default=18)
        parser.add_argument('tel',type=inputs.regex(r'\d+'),help='电话验证失败')
        parser.add_argument('birthday',type=inputs.date,help='电话验证失败')
        parser.add_argument('gender',type=str,help='性别验证失败',choices=['male','female','secret'])
        args=parser.parse_args()
        print(args)
        return args

api.add_resource(LoginView,'/login/')

# type可以指定为python自带类型，也可以使用flask_restful下面inputs里面的数据类型，会将提交上来的数据强制转化
# 常用类型有：url/regex/date 会将上传类型转换成datetime.date
# 注意input.date与from datetime import date【至少传三个参数-年月日】不一样，前者会自动将传入参数做与预处理，
# 后者只会将传入数据传给第一个关键词参数year报错。


@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
