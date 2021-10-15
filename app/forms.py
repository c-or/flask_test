from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField
from wtforms.validators import data_required

class loginForm(FlaskForm):
    user_name = StringField('name',validators=[data_required()])
    pass_word = StringField('PassWord',validators=[data_required()])
    remember_me = BooleanField('remember_me',default=False)
