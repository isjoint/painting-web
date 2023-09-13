"""
@date: 2023/9/11
@author: March
@desc: test

"""
from flask import Blueprint
user_bp = Blueprint("user_bp", __name__, url_prefix="/v1/")

from . import user






