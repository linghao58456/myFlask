"""
@author: hao.ling
@Date: 2020/7/24 11:02 下午
@Annotation: 初始化数据库连接
"""
import pymysql
from config.mysql import dbConfig


class initialization:
    def __init__(self):
        database = dbConfig()
        self.db = pymysql.Connect(host=database['host'], user=database['username'], password=database['password'],
                             port=database['port'], database=database['db'])
        self.cursor = self.db.cursor()