"""
@date: 2023/9/11
@author: March
@desc: test

"""
import hashlib
import random
import string
import requests
import time

def calculate_sign(appid, salt, secretkey):
    user_sign = appid + salt + secretkey
    m1 = hashlib.md5()
    m1.update(user_sign.encode(encoding='utf-8'))
    return m1.hexdigest()

length_of_string = random.randint(1, 10)
salt = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

appid = 'sc'
secretkey = '123456'
sign = calculate_sign(appid, salt, secretkey)


url = 'http://127.0.0.1:9000/v1/product'
params = {
    'appid': appid,
    'salt': salt,
    'sign': sign,
    #'timestamp': time.time()
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"请求失败，状态码：{response.status_code}")



