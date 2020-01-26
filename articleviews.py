from flask import Blueprint,render_template,make_response
from flask_restful import Api,Resource

article_bp=Blueprint('article',__name__,url_prefix='/article')
api=Api(article_bp)

@api.representation(mediatype='text/html')
def output_html(data,code,headers):
    print(type(data))
    resp=make_response(data)
    return resp

class ListView(Resource):
    def get(self):
        return render_template('list.html',user='hello')

api.add_resource(ListView,'/list/',endpoint='list')
