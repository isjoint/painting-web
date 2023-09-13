"""
@author: wy
@file: handler.py
@time: 2023/8/2 16:45
"""
from flask_restful import HTTPException
from libs.error_code import APIException

#无论什么异常  都返回APIException
def default_error_handler(ex):
    if isinstance(ex, APIException):
        return ex
    if isinstance(ex, HTTPException):
        code = ex.code
        message = ex.description
        status_code = 10001
        return APIException(code=code, message=message, status_code=status_code)
    print(type(ex))
    return APIException()
