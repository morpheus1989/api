from flask import Flask
import config
from exts import db
# 没有导入db下绑定的模型会报【INFO  [alembic.env] No changes in schema detected.】未检测到变化
# 原理，manage文件在导入app的时候会检测到需要同步数据库的模型，所以也可以在manage.py创建manager对象前导入
# from models import User
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    return 'you gey Hello World!'

@app.route('/profile/')
def profile():
    pass

if __name__ == '__main__':
    app.run()
