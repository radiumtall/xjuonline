from wtforms import StringField,SubmitField,PasswordField,SelectField
from wtforms.validators import  Required,DataRequired
from flask_wtf import FlaskForm
import datetime
#登录表单
class Login_Form(FlaskForm):
    username=StringField('username',validators=[Required()])
    password=PasswordField('password',validators=[Required()])
    submit=SubmitField('Login')
class Func_User(FlaskForm):
    stu_name=StringField('  学生姓名  ',validators=[Required()])
    status_1=SelectField('本人是否健康',validators=[DataRequired('默认')],choices=[('',''),('Yes','Yes'),('No','No')])
    status_2=SelectField('家人是否健康',validators=[DataRequired('默认')],choices=[('',''),('Yes','Yes'),('No','No')])
    status_3=SelectField('  是否返校  ',validators=[DataRequired('默认')],choices=[('',''),('Yes','Yes'),('No','No')])
    submit=SubmitField('提交')
class Func_Admin(FlaskForm):
    time = StringField('时间',validators=[Required()],default=str(datetime.date.today()))
    action =SelectField('Action',validators=[DataRequired('默认')],choices=[('view','view'),('download','download')])
    submit =SubmitField('Get It!')