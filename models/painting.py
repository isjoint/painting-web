"""
@date: 2023/9/11
@author: March
@desc: test
建立表模型
"""
import datetime
from . import db

# 用户信息表
class UserInfo(db.Model):
    __table__ = "user_info"
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    useracc = db.Column(db.Foreignkey("user_account.useracc_id"))
    namey = db.Column(db.String(128))
    age = db.Column(db.Integer)
    country = db.Column(db.String(128))
    email = db.Column(db.String(128))
    update_time = db.Column(db.DateTime(), default=datetime.datetime.now)

    paint_user = db.relationship("PaintInfo", backref="paintuser")
    reply_user = db.relationship("ReplyInfo", backref="replyuser")

    def keys(self):
        return 'namey', 'age', 'country', 'email'
    def __getitem__(self, item):
        return getattr(self, item)

# 用户账号信息表
class UserAccount(db.Model):
    __tablename__ = "user_account"
    useracc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(128))
    passwd = db.Column

# 插画信息表
class PaintInfo(db.Model):
    __tablename__ = "paint_info"
    paint_desc_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    paint_user_id = db.Column(db.Foreignkey("user_info.user_id"))
    paint = db.Column(db.Text)
    paint_desc = db.Column(db.String(256))
    likes = db.Column(db.Integer, default=0)
    collects = db.Column(db.Integer, default=0)

    com_paint = db.relationship("CommentInfo", backref="compaint")

    def keys(self):
        return 'paint_user_id', 'paint', 'paint_desc', 'likes', 'collects'
    def __getitem__(self, item):
        if item == 'paint_user_id':
            return self.painuser.namey
        else:
            return getattr(self, item)

# 评论表
class CommentInfo(db.Model):
    __tablename__ = "comment_info"
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.Text)
    com_paint_id = db.Column(db.Foreignkey("paint_info.paint_id"))
    com_user_id = db.Column(db.Foreignkey("user_info.user_id"))

    def keys(self):
        return 'comment', 'com_paint_id'
    def __getitem__(self, item):
        if item == 'com_paint_id':
            return self.compaint.paint
        else:
            return getattr(self, item)

# 回复表
class ReplyInfo(db.Model):
    __tablename__ = "reply_info"
    reply_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reply = db.Column(db.Text)
    reply_user_id = db.Column(db.Foreignkey("user_info.user_id"))
    reply_paint = db.Column(db.Foreignkey("paint_info.paint_desc_id"))

    def keys(self):
        return 'reply', 'reply_user_id'
    def __getitem__(self, item):
        if item == 'reply_user_id':
            return self.replyuser.namy
        else:
            return getattr(self, item)
