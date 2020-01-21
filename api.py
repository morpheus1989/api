from flask import Flask
import config
app = Flask(__name__)
app.config.from_object(config)

from exts import db
# 绑定
db.init_app(app)


@app.route('/')
def hello_world():
    return 'you gey Hello World!'

@app.route('/profile/')
def profile():
    pass


if __name__ == '__main__':
    app.run()
