"""
@date: 2023/9/1
@author: March
@desc: test

"""
import pymysql
from config.settings import DB_HOST, DB_PASS, DB_PORT, DB_USER, DB_SCHEM

def conn_mysql():
    conn = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        db=DB_SCHEM
    )

    return conn



