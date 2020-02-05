from flask_login import UserMixin
import sys
sys.path.append('../')
from app import db

class Users(UserMixin, db.Model):
    __tablename__ = 'users'  # 对应mysql数据库表
    Id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=True, index=True)
    stu_name = db.Column(db.String(64), unique=True, index=True)
    flag = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, username, password, flag, stu_name):
        self.username = username
        self.passwd = password
        self.flag = flag
        self.stu_name = stu_name
    def get_id(self):
        return self.Id

    def __repr__(self):
        return '<User %r>' % self.name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False