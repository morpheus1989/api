from flask import Flask,request,render_template
from wtforms import Form,StringField
from wtforms.validators import Length,EqualTo

class RegistForm(Form):
    # 导入验证器/处理条件,铲除一坨垃圾代码
    # Length注意使用关键字传参，避免导致At least one of `min` or `max` must be specified
    # validators接收验证列表
    user=StringField(validators=[Length(min=3,max=10,message='长度必须介于3-10之间')])
    password=StringField(validators=[Length(min=6,max=10)])
    password_repeat=StringField(validators=[Length(min=6,max=10),EqualTo('password',message='两次密码不一致')])

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'you gey Hello World!'

@app.route('/regist/',methods=['POST','GET'])
def regist():
    if request.method=='GET':
        return render_template('regist.html')
    else:
        form=RegistForm(request.form)
        # 使用validate查看验证结果
        if form.validate():
            return 'ok'
        else:
            # 使用errors查看错误信息，{'user': ['长度必须介于3-10之间']}
            error_msg=form.errors
            print(error_msg)
            return '；'.join(error_msg)

if __name__ == '__main__':
    app.run(debug=True)
