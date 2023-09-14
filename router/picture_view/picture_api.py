"""
@date: 2023/9/5
@author: March
@desc: test

"""
# restful --> 接口规范，接口设计风格
# 设计一个接口
# 数据返回
# 接收数据的方式
# url，方法

#    统一风格
# rest -- 表现层状态转移
# web -- 每一类页面 -- 资源
# 资源 通过http的动作来实现状态转移 GET,PUT,POST,DELETE

# /{version}/{resources}/{resource_id}

# restful api 设计
# /v1/product  POST 新增
#              GET  查询所有
# /v1/product/id     PUT     修改
#                    DELETE  删除
#                    GET     查询某一个

from flask import Blueprint, request
from flask_restful import Api, Resource
from libs.response import generate_response
from . import picture_bp
from models.painting import db
from libs.authorization import auth_required
from libs.handler import default_error_handler
from models.painting import PaintInfo

# 将restful api对象和蓝图绑定
api = Api(picture_bp)
api.handle_error = default_error_handler

class PictureView(Resource):
    #@装饰器
    @auth_required
    def get(self, id=None):
        if id is None:
            result = PaintInfo.query.all()
        else:
            result = PaintInfo.query.filter(PaintInfo.paint_desc_id == id).all()
        if result:
            result2 = [dict(pro) for pro in result]
            return generate_response(message="get sucess!", data=result2)
        else:
            return generate_response(code=1, message="get fail!")

    def post(self):
        paint_url = request.json.get("painturl")
        paint_uid = request.json.get("paintuserid")
        paint_desc = request.json.get("paintdesc")
        if paint_url and paint_uid and paint_desc:
            paintinfo = PaintInfo(paint=paint_url,
                                  paint_desc=paint_desc,
                                  paint_user_id=paint_uid)
            db.session.add(paintinfo)
            db.session.commit()
            return generate_response(message="commit success!")
        return generate_response(message="commit fail!", code=10002)

    def put(self, id):
        product_id = PaintInfo.query.get(id)
        if product_id:
            # 全部提交到数据库
            paint_url = request.json.get("painturl")
            paint_uid = request.json.get("paintuserid")
            paint_desc = request.json.get("paintdesc")
            paintinfo = PaintInfo(paint=paint_url,
                                  paint_desc=paint_desc,
                                  paint_user_id=paint_uid)
            db.session.add(paintinfo)
            db.session.commit()
            return generate_response(message="commit success!")
        return generate_response(message="commit fail", code=1)

    def delete(self, id):
        paint_desc_id = PaintInfo.query.get(id)
        if paint_desc_id:
            # 提交到数据库
            db.session.delete(paint_desc_id)
            db.session.commit()
            return generate_response(message="commit success!")
        return generate_response(message="commit fail", code=1)

api.add_resource(PictureView, "/picture")
api.add_resource(PictureView, "/picture/<id>", endpoint="paint_id")



