"""
@author: hao.ling
@Date: 2020/8/16 4:51 下午
@Annotation: 配置中心表操作
"""
from database.initialization import initialization


class Configuration(initialization):
    # 配置中心操作
    def select_system_name(self, systemName):
        """
        查询系统名称
        :param systemName: 系统名称
        :return:
        """
        self.cursor.execute("select * from system where system_name='{}' and status='0'".format(systemName))
        result = self.cursor.fetchall()
        return result

    def insert_system(self, systemName, systemPath, userId):
        """
        新增系统
        :param systemName: 系统名称
        :param systemPath: 系统地址
        :param userId: 创建者id
        :return:
        """
        try:
            self.cursor.execute(
                "insert into system (system_name,system_path,creatorId) values ('{}','{}','{}')"
                    .format(systemName, systemPath, userId))
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(str(e))
            return False
