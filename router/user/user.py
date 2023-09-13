"""
@date: 2023/9/11
@author: March
@desc: test

"""
from flask import request

from forms.user import UserForm, LoginForm
from libs.authorization import create_token
from libs.handler import default_error_handler
from . import user_bp
from flask_restful import Resource, Api
from models.user import User
from libs.response import generate_response

api = Api(user_bp)

api.handle_error = default_error_handler

class UserRegister(Resource):
    # post方法
    # 做了数据校验版本
    def post(self):
        #try:
            data = request.json
            form = UserForm(data=data)
            if form.validate():
                User.create_user(username=data.get("username"),
                                 password=form.password.data)
                return generate_response(message="注册成功", code=0)
            else:
                return generate_response(code=1, message=form.errors)

api.add_resource(UserRegister, "/user")

# 登录视图
class LoginView(Resource):
    def post(self):
        data = request.json
        form = LoginForm(data=data)
        user = form.validate()
        if user:
            # 验证通过，生成token
            token = create_token(user.id)
            return generate_response(message="login success", code=0, data={"token": token})
        else:
            return generate_response(message="login fail", code=1)

api.add_resource(LoginView, "/login")


