from flask import Flask
import config
from exts import db
from articleviews import article_bp

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
app.register_blueprint(article_bp)
# api=Api(app)


@app.route('/')
def index():
    return 'ok'


if __name__ == '__main__':
    app.run()
