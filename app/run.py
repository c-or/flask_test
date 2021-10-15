from app import app
from app import db,modules
if(__name__=='__main__'):
    db.drop_all()
    db.create_all()
    u1 = modules.User(name='user_a',email='user_a@163.com')
    u2 = modules.User(name='user_b',email='user_b@163.com')
    db.session.add_all([u1,u2])
    db.session.commit()
    app.run(debug=True)

