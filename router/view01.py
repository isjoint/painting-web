"""
@date: 2023/8/31
@author: March
@desc: test

"""
# 管理视图
from flask import Blueprint, render_template

view01_bp = Blueprint("view01", __name__, url_prefix="/v1/")

@view01_bp.route("/index")
def index():
    return "this is index"

@view01_bp.route("/index2")
def index2():
    # render_template  页面渲染函数
    return render_template("index.html", message="hello world")



