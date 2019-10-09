from datetime import datetime
from app import db
from sqlalchemy.orm import validates

class Base(db.Model):
    __abstract__ = True

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @validates('email')
    def validate_email(self, key, address):
        assert '@' in address, 'Email should contain @'
        return address

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(Base):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    @validates('user_id')
    def validate_email(self, key, user_id):
        assert user_id != None, 'User must be filled!!'
        return user_id

    def __repr__(self):
        return '<Post {}>'.format(self.body)