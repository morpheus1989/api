from flask import Flask,request,current_app,url_for,g
import config
from logs import log
app = Flask(__name__)
app.config.from_object(config)
# 先看结果后讲原理，内容太抽象吃不消

# 手动创建上下文，将其加入栈中
# app_content=app.app_context()
# app_content.push()
# print(current_app.name)

# with语句内部也可以拥有app上下文
# with app.app_context():
#     print(current_app.name)

# 网络请求会自动创建应用上下文
@app.route('/')
def hello_world():
    user=request.args.get('user')
    # g对象在flask应用运行期间都可以使用，也是线程隔离的
    # 专门存储开发者自己定义的一些数据，方便其他地方调用
    # 无需传参，更加方便
    g.user=user
    log()
    return user or 'no user'

@app.route('/list/')
def list():
    return 'list log'
# 在视图函数中，不用担心上下文问题，因为通过url访问的方式执行时，
# flask底层自动会给栈中推入上下文
# app和请求分别有一个堆栈【localstack】；local表明对象具有线程隔离的特性
# url_for 先获取app上下文，然后检查请求上下文；
# app/request的相关操作都需要上下文支持
# 使用test_request_context自动创建请求上下文时，先检查应用上下文，没有就自动推入一个；
with app.test_request_context():
    print(url_for('list'))

# 疑问，为什么要把上下文推入栈中，直接创建上下文不好么？？
# 因为在flask中不仅仅只创建一个app，多个app使用栈来分别管理
# 当前app或者正在使用的app，肯定在栈顶【top】，用完出栈【从栈顶部移除】就行
# 同理，测试代码/离线脚本/多个视图，需要创建多个请求上下文

if __name__ == '__main__':
    app.run()
