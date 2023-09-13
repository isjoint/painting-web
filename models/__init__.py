"""
@date: 2023/9/2
@author: March
@desc: test

"""
# flask_sqlalchemy --> 创建对象关系映射
from flask_sqlalchemy import SQLAlchemy

# 生成对象关系实例
db = SQLAlchemy()

def init_app_db(app):
    db.init_app(app)

from . import product
from . import user


