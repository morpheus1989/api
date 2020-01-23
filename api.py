from flask import Flask,request,Response
from datetime import datetime,timedelta
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    resp=Response('blog index')
    # 设置cookie
    resp.set_cookie('user','spider')
    expires=datetime.now()+timedelta(days=1)
    # 主域名前面加个点
    resp.set_cookie('work','18',expires=expires,domain='.blog.com')
    return resp


if __name__ == '__main__':
    app.run()
