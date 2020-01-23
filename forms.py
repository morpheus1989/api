from wtforms import Form, StringField, FloatField
from wtforms.validators import Email, Length, EqualTo, InputRequired,NumberRange
from models import User


class RegistForm(Form):
    email = StringField(validators=[Email()])
    user = StringField(validators=[Length(3, 20)])
    pwd = StringField(validators=[Length(6, 20)])
    pwd_repeat = StringField(validators=[EqualTo('pwd')])
    deposit = FloatField(validators=[InputRequired()])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    pwd = StringField(validators=[Length(6, 20)])
    # def validate(self):
    #     result=super(LoginForm, self).validate()
    #     if not result:
    #         return False
    #     email=self.email.data
    #     pwd=self.pwd.data
    #     user=User.query.filter(User.email==email,User.pwd==pwd).first()
    #     if not user:
    #         return self.email.errors.append('邮箱或者密码错误')
    #     return True
class TransferForm(Form):
    email = StringField(validators=[Email()])
    # 表单验证会自动将前端提交的文本数据转换成对应类型
    money = FloatField(validators=[NumberRange(1,100000)])