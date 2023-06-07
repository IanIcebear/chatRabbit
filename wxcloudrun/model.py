from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())

# 缓存表
class Answer(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Answer'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    # 请求状态，status=0是成功，1是等待中
    status = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    answer =  db.Column(db.String)

