from wtforms import Form,StringField,FloatField
from wtforms.validators import Email,Length,EqualTo,InputRequired
class RegistForm(Form):
    email=StringField(validators=[Email()])
    user=StringField(validators=[Length(3,20)])
    pwd=StringField(validators=[Length(6,20)])
    pwd_repeat=StringField(validators=[EqualTo('pwd')])
    deposit=FloatField(validators=[InputRequired()])