"""
@author: hao.ling
@Date: 2020/7/24 10:52 下午
@Annotation: 数据库配置
"""


def dbConfig():
    host = "localhost"
    username = "root"
    password = "12345678"
    dbName = "testPlatform"
    port = 3306
    return {"host": host, "username": username, "password": password, "db": dbName, "port": port}

def checkValue():
    return "myTest"