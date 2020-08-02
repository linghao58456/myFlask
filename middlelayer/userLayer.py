"""
@author: hao.ling
@Date: 2020/7/25 9:25 上午
@Annotation: 用户信息表中间层操作
"""
from database.user import User
from encryption.makeMD5 import md5


class UserLayer:
    # 用户中间层操作
    def __init__(self):
        self.user = User()

    def select_user(self, username):
        """
        查询用户
        :param username: 用户名
        :return:
        """
        result = self.user.select_user(username=username)
        if len(result) > 0:
            user_list = {}
            for res in result:
                user_list.update({"userId": res[0], "username": res[1]})
            return {"code": 1000, "data": user_list, "message": "获取成功"}
        return {"code": 9999, "data": "", "message": "用户不存在"}

    def insert_user_info(self, username, password):
        """
        新增插入用户信息
        :param username: 用户名
        :param password: 密码
        :return:
        """
        result = self.select_user(username=username)
        if result['code'] == 9999:
            pwd = md5(password=password)
            response = self.user.insert_user(username=username, password=pwd)
            if response:
                result = self.select_user(username=username)
                return {"code": 1000, "data": result['data'], "message": "注册成功"}
            return {"code": 9999, "data": "", "message": "注册失败，请重新注册"}
        return {"code": 9999, "data": result['data'], "message": "用户已存在"}

    def update_user_password(self, username, newPassword):
        """
        更新用户密码
        :param username: 用户名
        :param newPassword: 新密码
        :return:
        """
        result = self.select_user(username=username)
        if result['code'] == 1000:
            pwd = md5(password=newPassword)
            response = self.user.update_user_password(username=username, password=pwd)
            if response:
                return {"code": 1000, "data": "", "message": "修改成功,请登录"}
            return {"code": 9999, "data": "", "message": "修改失败，请重新操作"}
        return result

    def select_username_password(self, username, password):
        """
        查询用户密码
        :param username: 用户名
        :param password: 密码
        :return:
        """
        result = self.user.select_user(username=username)
        pwd = md5(password=password)
        if len(result) > 0:
            for res in result:
                user_list = {}
                if pwd == res[2]:
                    user_list.update({"userId": res[0], "username": res[1]})
                    return {"code": 1000, "data": user_list, "message": "登录成功"}
                return {"code": 9999, "data": "", "message": "账号或密码错误"}
        return {"code": 9999, "data": "", "message": "账户不存在"}

    def change_user_password(self, username, oldPassword, newPassword):
        """
        修改用户密码
        :param username: 用户名
        :param oldPassword: 旧密码
        :param newPassword: 新密码
        :return:
        """
        result = self.select_username_password(username=username, password=oldPassword)
        if result['code'] == 1000:
            response = self.update_user_password(username=username, newPassword=newPassword)
            return response
        return {"code": 9999, "data": "", "message": "旧密码错误,请重新输入"}
