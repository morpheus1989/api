import re

from flask import Flask,request,render_template,send_from_directory
from werkzeug.utils import secure_filename

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
        desc=request.form.get('desc')
        avatar=request.files.get('avatar')
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

# 下载/获取图片
@app.route('/download/<filename>/')
def download(filename):
    return send_from_directory(UPLOAD_PATH,filename)


if __name__ == '__main__':
    app.run(debug=True)
