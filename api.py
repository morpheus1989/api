from flask import Flask
import config
from exts import db
from models import User,Article,Tag
from flask_restful import Api,Resource,fields
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
api=Api(app)


class ArticleView(Resource):

    resource_fields={
        'title':fields.String}

    def get(self,article_id):
        article=Article.query.get(article_id)
        return article

api.add_resource(ArticleView,'/article/<article_id>/',endpoint='article')

@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run()
