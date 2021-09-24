from flask. import form
from wtforms import StringField,BooleanField
from wtforms.validators import data_required

class loginForm():
    openid = StringField('openid',validators=[data_required()])
    remember_me = BooleanField('remember_me',default=False)
