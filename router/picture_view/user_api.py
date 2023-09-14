"""
@date: 2023/9/14
@author: March
@desc: test

"""
from flask import request
from flask_restful import Api, Resource
from libs.response import generate_response
from . import picture_bp
from models.painting import db
from libs.authorization import auth_required
from libs.handler import default_error_handler
from models.painting import UserInfo, PaintInfo

# 将restful api对象和蓝图绑定
api = Api(picture_bp)
api.handle_error = default_error_handler

class UserView(Resource):
    def get(self, id=None):
        if id is None:
            # id为none则返回插画信息
            result = PaintInfo.query.all()
        else:
            result = UserInfo.query.filter(UserInfo.user_id == id).all()
        if result:
            result2 = [dict(pro) for pro in result]
            return generate_response(message="get sucess!", data=result2)
        else:
            return generate_response(code=1, message="get fail!")

    def post(self):
        nick_name = request.json.get("nickname")
        user_age = request.json.get("userage")
        user_country = request.json.get("usercountry")
        useremail = request.json.get("useremail")
        if nick_name and user_age and user_country and useremail:
            userinfo = PaintInfo(namey=nick_name,
                                 age=user_age,
                                 country=user_country,
                                 email=useremail)
            db.session.add(userinfo)
            db.session.commit()
            return generate_response(message="commit success!")
        return generate_response(message="commit fail!", code=10002)

    @auth_required
    def put(self, id):
        user_id = UserInfo.query.get(id)
        if user_id:
            # 全部提交到数据库
            nick_name = request.json.get("nickname")
            user_age = request.json.get("userage")
            user_country = request.json.get("usercountry")
            useremail = request.json.get("useremail")
            if nick_name and user_age and user_country and useremail:
                userinfo = PaintInfo(namey=nick_name,
                                     age=user_age,
                                     country=user_country,
                                     email=useremail)
                db.session.add(userinfo)
            db.session.commit()
            return generate_response(message="commit success!")
        return generate_response(message="commit fail", code=1)

    @auth_required
    def delete(self, id):
        user_id = PaintInfo.query.get(id)
        if user_id:
            # 提交到数据库
            db.session.delete(user_id)
            db.session.commit()
            return generate_response(message="commit success!")
        return generate_response(message="commit fail", code=1)

api.add_resource(UserView, "/userinfo")
api.add_resource(UserView, "/userinfo/<id>", endpoint="user_id")
