from flask_script import Manager
db_manager=Manager()

@db_manager.command
def init():
    print('初始化成功')