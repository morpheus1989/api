from flask import Flask
import config
from exts import db
# 没有导入db下绑定的模型会报【INFO  [alembic.env] No changes in schema detected.】未检测到变化
from models import User
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
