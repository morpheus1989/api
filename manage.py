from flask_script import Manager
from api import app
from exts import db
from flask_migrate import Migrate,MigrateCommand
from models import User
manager=Manager(app)
# 绑定app和数据库
Migrate(app,db)
# 添加migrate所有的子命令绑定到db下
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()