"""
@author: hao.ling
@Date: 2020/8/23 7:27 下午
@Annotation: 配置中心接口
"""

from flask import jsonify, request

from api import api

from middlelayer.configurationLayer import ConfigurationLayer

config = ConfigurationLayer()


# 查询系统名称
@api.route("/configuration/detail", methods=["GET"])
def get_configuration_detail():
    response = request.args.get("systemName")
    result = config.select_system(systemName=response)
    return jsonify(result)
