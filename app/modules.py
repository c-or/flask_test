from app import db

class User(db.Model):
    id = db.Column(db.INTEGER,primary_key=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(50),index=True,unique=True)
    email = db.Column(db.String(50),index=True,unique=True)
    # __repr__方法返回的是对象的属性信息，如果不重写该方法，那么在直接打印对象信息时显示的是对象的内存信息，重写后显示的是该方法的返回信息

    @property
    def is_authenticated(self):
        return True

    @property
    def is_activated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


    def __repr__(self):
        return '<User %r>' % (self.name)
