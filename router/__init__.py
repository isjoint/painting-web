"""
@date: 2023/8/31
@author: March
@desc: test

"""
from .view01 import view01_bp
from .user import user_bp

def init_app(app):
    app.register_blueprint(view01_bp)
    app.register_blueprint(user_bp)









