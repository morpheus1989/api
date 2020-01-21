from wtforms import Form,StringField,IntegerField,ValidationError,BooleanField
from wtforms.validators import Length,EqualTo,Email,InputRequired,NumberRange,Regexp,URL,UUID

class RegistForm(Form):
    # 导入验证器/处理条件,铲除一坨垃圾代码
    # Length注意使用关键字传参，避免导致At least one of `min` or `max` must be specified
    # validators接收验证列表
    user=StringField(validators=[Length(min=3,max=10,message='长度必须介于3-10之间')])
    # 使用【validate_字段名】来进行自定义验证器，会被自动识别来执行，不符合条件可以抛出异常；常用于验证码captcha
    def validate_user(self,field):
        if field.data !='hero':
            raise ValidationError('用户输入错误')

    password=StringField(validators=[Length(min=6,max=10)])
    password_repeat=StringField(validators=[Length(min=6,max=10),EqualTo('password',message='两次密码不一致')])

class SettingForm(Form):
    # 第一个参数用来指定label
    user=StringField('用户名：',validators=[IntegerField()])
    # 用户勾选，不需要验证
    remember=BooleanField('记住我：')