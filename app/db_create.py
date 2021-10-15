from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from app import db
from modules import User

db.create_all()

def check_pwd(username,pwd):
    password = db.Query(User).filter(name=username).first()
    if(password==pwd):
        return True
    else:
        return False