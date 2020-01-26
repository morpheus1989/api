
from exts import db

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))
    email=db.Column(db.String(50))


article_tag_table=db.Table('article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key=True),
)


class Article(db.Model):
    __tablename__='article'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    # db.text ;指定字段类型错误 SchemaItem' object, such as a 'Column' or a 'Constraint' expected
    content=db.Column(db.Text)
    author_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    author=db.relationship('User',backref='articles')
    tags=db.relationship('Tag',secondary=article_tag_table,backref='articles')

class Tag(db.Model):
    __tablename__ = 'tag'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50))

