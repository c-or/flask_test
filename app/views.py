from flask import render_template,flash,redirect
from .forms import loginForm
from app import app,lm
from .modules import User
from db_create import *

@app.route('/')
@app.route('/index')
def index():
    user = {'name':'jack'}
    posts=[{'author':'john','body':'Beautiful day in Portland!'},
           {'author':'Susan','body':'The Avengers movie was so cool!'}]
    return render_template("index.html",user=user,posts=posts)

@app.route('/login',methods=['get','post'])
def login():
    form = loginForm()
    username = form.user_name
    password = form.pass_word
    status = check_pwd(username,password)
    if (status):
        return redirect('/index')

    # 判断数据是否合法
    if(form.validate_on_submit()):
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='sign in',form=form)

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

