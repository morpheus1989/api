from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(50),nullable=False)
    age=db.Column(db.Integer,default=0)

    def __repr__(self):
        return '{}->{}'.format(self.id,self.name)