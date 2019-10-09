from app import db
from app.models import User
from app import utils

def add(user_dict):
    u = User(id=user_dict['id'], username=user_dict['username'], email=user_dict['email'])
    db.session.add(u)
    db.session.commit()

def delete(id):
    User.query.filter(User.id == id).delete()
    db.session.commit()    

def get(id):
    u = User.query.get(id)
    return(utils.row2dict(u))

def get_all():
    users = User.query.all()
    return([utils.row2dict(u) for u in users])


