from flask_login import UserMixin
import sys
sys.path.append('../')
from app import db

class Datas(UserMixin, db.Model):
    __tablename__ = 'datas'  # 对应mysql数据库表
    
    Id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # 本人是否健康
    status_1 = db.Column(db.String(64), unique=True, index=True)
    # 家人是否健康
    status_2 = db.Column(db.String(64), unique=True, index=True)
    # 是否返校
    status_3 = db.Column(db.String(64), unique=True, index=True)
    stu_name = db.Column(db.String(64), unique=True, index=True)
    def __init__(self, time, username, status_1, status_2, status_3, stu_name):
        self.time = time
        self.username = username
        self.status_1 = status_1
        self.status_2 = status_2
        self.status_3 = status_3
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