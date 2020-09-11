"""
@author: hao.ling
@Date: 2020/7/24 10:48 下午
@Annotation: 蓝图注册
"""
from flask import Blueprint

api = Blueprint("api", __name__)

from api import errors, userView, configurationView
