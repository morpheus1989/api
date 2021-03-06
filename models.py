from  flask_sqlalchemy import SQLAlchemy
from api import app
db=SQLAlchemy(app)
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    city=db.Column(db.Enum('上海','广州','西安'),default='西安')
    age=db.Column(db.Integer,default=0)

    def __repr__(self):
        return '{}->{}'.format(self.id,self.name)