from flask import Flask,request,render_template
from forms import RegistForm,SettingForm

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

@app.route('/setting/',methods=['POST','GET'])
def setting():
    if request.method=='GET':
        # 将表单渲染到前端，自动生成input代码
        form=SettingForm()
        return render_template('setting.html',form=form)
    else:
        return 'ok'

if __name__ == '__main__':
    app.run(debug=True)
