import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

basedir = os.path.abspath(__file__)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Loreal01~@139.196.223.204:3306/test?charset=utf8'
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')