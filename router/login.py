"""
@date: 2023/8/31
@author: March
@desc: test

"""
from flask import Blueprint, request
from config.settings import user_dict
from libs.response import generate_response

login_bp = Blueprint("login", __name__, url_prefix="/v1/")

@login_bp.route("/login")
def login():
    user = request.json.get("username")
    passwd = request.json.get("passwd")
    # cur_user = user_dict.get(user)
    if user == user_dict["username"] and passwd == user_dict["passwd"]:
        return generate_response(message="login success")
    return generate_response(message="login fail", code=1)
