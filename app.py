"""
@date: 2023/9/11
@author: March
@desc: test

"""
from flask import Flask
import os

def create_app():
    my_app = Flask(__name__)
    my_app.config.from_object('config.settings')

    # 从环境变量里读取
    # if 'FLASK_CONF' in os.environ:
    #     my_app.config.from_envvar('FLASK_CONF')

    return my_app
