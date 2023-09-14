"""
@date: 2023/9/11
@author: March
@desc: test

"""
from flask import Blueprint
picture_bp = Blueprint("picture_bp", __name__, url_prefix="/v1/")
# 导入在下面
from . import picture_api
from . import user_api

