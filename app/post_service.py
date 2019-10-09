from app import db
from app.models import User, Post
import dateutil.parser
from app import utils

def add(post_dict):
    u = User.query.get(post_dict['user_id'])
    post_date_time = dateutil.parser.parse(post_dict['timestamp'])
    p = Post(id=post_dict['id'], body=post_dict['body'], timestamp=post_date_time, author=u)
    db.session.add(p)
    db.session.commit()

def delete(id):
    User.query.filter(Post.id == id).delete()
    db.session.commit()    

def get(id):
    p = Post.query.get(id)
    return(utils.row2dict(p))

def get_all():
    posts = Post.query.all()
    return([utils.row2dict(p) for p in posts])

       

