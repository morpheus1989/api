from flask_script import Manager
from api import app
from models import User,db
from db_script import db_manager
manager=Manager(app)
manager.add_command('db',db_manager)

@manager.command
def greet():
    return 'hey'

@manager.option('-n','--name',dest='name')
def add_user(name):
    pass
    user=User(name=name)
    db.session.add(user)
    db.session.commit()
    print('添加成功')

if __name__ == '__main__':
    manager.run()