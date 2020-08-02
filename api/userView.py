"""
@author: hao.ling
@Date: 2020/7/26 2:29 下午
@Annotation: 用户接口
"""
from flask import jsonify, request

from api import api

from middlelayer.userLayer import UserLayer

user = UserLayer()


# 注册
@api.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    response = user.insert_user_info(username=data['username'], password=data['password'])
    return jsonify(response)


# 查询用户
@api.route("/searchUser", methods=["GET"])
def search_user():
    data = request.args.get("username")
    response = user.select_user(data)
    return jsonify(response)


# 重置密码
@api.route("/forgetPassword", methods=["POST"])
def forget_password():
    data = request.get_json()
    response = user.update_user_password(data['username'], data['password'])
    return jsonify(response)


# 登录
@api.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    response = user.select_username_password(username=data['username'], password=data['password'])
    return jsonify(response)


# 修改密码
@api.route("/changePwd", methods=["POST"])
def change_password():
    data = request.get_json()
    response = user.change_user_password(username=data['username'], oldPassword=data['oldPassword'],
                                         newPassword=data['newPassword'])
    return jsonify(response)
