import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir


app = Flask(__name__)
#从当前配置文件中读取配置信息
app.config.from_object('config')
db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
# 该导入语句不可放到app赋值语句前面，因为views中需要用到app变量
from app import views
from app import modules