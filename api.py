import re

from flask import Flask,request,render_template,send_from_directory
# 文件名安全检查
from werkzeug.utils import secure_filename
# 将两个不可变的字典合并起来
from werkzeug.datastructures import CombinedMultiDict
# 导入验证表单
from forms import UploadForm
import os
UPLOAD_PATH=os.path.join(os.path.dirname(__file__),'static/images')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'you gey Hello World!'

@app.route('/upload/',methods=['POST','GET'])
def upload():
    if request.method=='GET':
        return render_template('upload.html')
    else:
        # 留意传参类型,将两个不可变打包起来，统一验证
        form=UploadForm(CombinedMultiDict([request.files,request.form]))
        if form.validate():
            # 合并后提供了第二种获取数据的方式,验证通过后，在form中获取
            # desc=request.form.get('desc')
            # avatar=request.files.get('avatar')
            desc = form.desc.data
            avatar = form.avatar.data
            # 网络，安全隐患无处不在
            # 对于文件名做安全检测，以防黑客攻击；linux ../../User/.bashrc，直接覆盖就哭鼻子了
            # 对中文文件名支持的不好，会直接剔除掉，可以自行处理
            origin_name=avatar.filename
            # 处理的小demo
            if re.match('[a-z]',origin_name):
                filename=secure_filename(origin_name)
            else:
                filename=origin_name
            avatar.save(os.path.join(UPLOAD_PATH,filename))
            return desc
        else:
            print(form.errors)
            return 'no'


if __name__ == '__main__':
    app.run(debug=True)
