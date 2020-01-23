host, port, user, password, db = '127.0.0.1', '3306', 'root', '123456', 'flask_icbc'
DB_CONFIG = dict(host=host, port=port, user=user, password=password, database=db)
DB_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(**DB_CONFIG)
SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=False