"""
@author: hao.ling
@Date: 2020/7/25 9:19 上午
@Annotation: 用户信息表操作
"""
from database.initialization import initialization


class User(initialization):
    # 用户信息sql
    def set_user_id(self):
        """
        设置user_id从10001开始
        :return: True，异常时False
        """
        try:
            self.cursor.execute("alter table users AUTO_INCREMENT=10001;")
            self.db.commit()
        except Exception as e:
            print(str(e))
            self.db.rollback()

    def select_user(self, username):
        """
        查询用户
        :param username: 用户名
        :return:
        """
        self.cursor.execute("select * from users where username='{}' and status=0;".format(username))
        result = self.cursor.fetchall()
        return result

    def insert_user(self, username, password):
        """
        插入用户
        :param username: 用户名
        :param password: 密码
        :return:
        """
        try:
            self.cursor.execute(
                "insert into users (username,password) values ('{}','{}')".format(username, password))
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False

    def update_user_password(self, username, password):
        """
        更新用户密码
        :param username: 用户名
        :param password: 密码
        :return:
        """
        try:
            self.cursor.execute(
                "update users set password='{}' where username='{}' and status=0".format(password, username))
            self.db.commit()
            return True
        except Exception as e:
            print(str(e))
            self.db.rollback()
            return False
