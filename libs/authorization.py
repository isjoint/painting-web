"""
@date: 2023/9/11
@author: March
@desc: test

"""
import time
from hashlib import md5  # 单向加密
from flask import request, current_app

from libs.error_code import TokenFailException
from models.user import ApiToken
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from libs.error_code import AuthorizedFailException

def auth_required(func):
    def inner(*args, **kwargs):
        api_flag = request.args.get("api")
        if (api_flag == "1" and api_auth()) or token_auth():
            return func(*args, **kwargs)
        else:
            raise AuthorizedFailException
    return inner

#api授权认证函数 -- 函数返回为真表示认证成功
def api_auth():
    params = request.args
    appid = params.get("appid")
    salt = params.get("salt")  # 盐值
    sign = params.get("sign")  # 签名

    api_token = ApiToken.query.filter_by(appid=appid).first()
    if not api_token:
        return False

    if not has_permission(api_token, request.path, request.method.lower()):
        return False
    # 获取数据库里的密钥
    secretkey = api_token.secretkey
    # 生成服务端的签名
    user_sign = appid + salt + secretkey
    m1 = md5()
    m1.update(user_sign.encode(encoding="utf-8"))
    # 判断客户端传递过来的签名和服务端生成签名是否一致
    if sign != m1.hexdigest():
        return False
    else:
        return True


# url验证
# api_token表记录
# url  客户端请求过来的路径
# method  客户端请求过来的方法
def has_permission(api_token, url, method):
    # 客户端请求的方法和url
    mypermission = method + url
    # 获取此api_token对象的所有url权限
    all_permission = [permission.method_type + permission.url
                      for permission in api_token.manage]
    if mypermission in all_permission:
        return True
    else:
        return False

def create_token(uid):
    # 生成token
    expir_in = current_app.config.get("EXPIRES_IN")
    payload = {"uid": uid, "exp": time.time() + expir_in}
    print(payload)
    key = current_app.config["SECRET_KEY"]
    token = jwt.encode(payload, key)
    return token

# 验证token
def token_auth():
    token = request.headers.get("token")
    if token:
        try:
            print(time.time())
            jwt_obj = jwt.decode(token, current_app.config.get("SECRET_KEY"), algorithms=["HS256"])
        except InvalidSignatureError as e:
            print("token不合法", e)
            raise TokenFailException
        except ExpiredSignatureError as e:
            print("token过期", e)
            raise TokenFailException
        return True
    else:
        return False






