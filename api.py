from flask import Flask,request,Response
from datetime import datetime,timedelta
import config
app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def hello_world():
    resp=Response('Hello World!')
    # 设置cookie
    resp.set_cookie('user','spider')
    expires=datetime.now()+timedelta(days=1)
    resp.set_cookie('work','18',expires=expires)

    return resp

@app.route('/del/')
def del_cookie():
    resp=Response('ok')
    # 删除cookie
    resp.delete_cookie('user')
    return resp

if __name__ == '__main__':
    app.run()
