from wtforms import Form,FileField,StringField
from wtforms.validators import InputRequired

from flask_wtf.file import FileRequired,FileAllowed
class UploadForm(Form):
    # 黑客喜欢在上传的文件上做文章，验证文件上传是否为空，已经指定格式
    avatar=FileField('肖像',validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    desc=StringField('描述',validators=[InputRequired()])

