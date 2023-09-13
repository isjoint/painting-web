"""
@date: 2023/8/31
@author: March
@desc: test

"""
from .view01 import view01_bp
from .login import login_bp
from .register import register_bp
from .product_view import product_bp
from .user import user_bp

def init_app(app):
    app.register_blueprint(view01_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(user_bp)

# 标准化返回 -- json格式
# 包括三个字段：data, code, msg
# data -- 返回的数据
# code -- 应用状态码
# msg -- 返回的说明








