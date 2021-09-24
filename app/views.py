from flask import render_template,flash,redirect
from app import app
from .forms import loginForm

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
    return render_template('login.html',title='sign in',form=form)