"""
api授权表
"""
from models import db
from werkzeug.security import generate_password_hash
import datetime

# API授权表的模型
app_permission = db.Table("app_permission",
                          db.Column("api_id", db.ForeignKey("api_token.id")),
                          db.Column("permission_id", db.ForeignKey("api_permission.id"))
                          )


# api_token表
# 存放的是授权密钥，以及授权id
class ApiToken(db.Model):
    __tablename__ = "api_token"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appid = db.Column(db.String(128), nullable=False)
    secretkey = db.Column(db.String(128), nullable=False)
    # 通过中间表去创建多对多的关系
    manage = db.relationship("ApiPermission", secondary=app_permission, backref="token")


# 存放的是授权的url
class ApiPermission(db.Model):
    __tablename__ = "api_permission"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    url = db.Column(db.String(128), nullable=False)
    method_type = db.Column(db.String(128), nullable=False)

class User(db.Model):
    __tablename__ = "userdb"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    _password = db.Column("password", db.String(128), nullable=False)
    role = db.Column(db.Integer, default=0)
    add_time = db.Column(db.DateTime, default=datetime.datetime.now)

    # property python内置装饰器，属性包装装饰器
    # 作用：把方法当做属性一样使用
    # 定义属性之前做一些检测，转换
    @property  # 自动根据函数名生成两个装饰器 --> password.setter password.deleter
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)

    @classmethod  # 类方法，第一个参数表示类本身
    def create_user(cls, username, password):
        user = cls()  # 创建实例对象
        user.username = username
        user.password = password
        db.session.add(user)
        db.session.commit()
