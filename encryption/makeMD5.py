"""
@author: hao.ling
@Date: 2020/7/26 2:36 下午
@Annotation: md5加密
"""
import hashlib

from config.mysql import checkValue


def md5(password):
    """
    md5加密
    :param password: 密码
    :return:
    """
    key = checkValue()
    value = key + str(password)
    result = hashlib.md5(value.encode("utf-8")).hexdigest()
    return result.upper()
