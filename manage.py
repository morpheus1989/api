
from  flask_script import Manager
from ICBC import app
from exts import db
from models import User
from flask_migrate import Migrate,MigrateCommand

manager=Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()