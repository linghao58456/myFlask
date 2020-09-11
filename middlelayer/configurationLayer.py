"""
@author: hao.ling
@Date: 2020/8/23 1:13 下午
@Annotation: 配置中心
"""
from database.configuration import Configuration


class ConfigurationLayer:
    def __init__(self):
        self.config = Configuration()

    def select_system(self, systemName):
        """
        查询系统配置信息
        :param systemName: 系统名称
        :return:
        """
        result = self.config.select_system_name(systemName=systemName)
        if len(result) > 0:
            response = {}
            for res in result:
                response.update({"id": res[0], "system_name": res[1], "system_path": res[2], "creatorId": res[4],
                                 "createTime": res[6], "modifyTime": res[7]})
            return {"code": 1000, "data": response, "message": "获取成功"}
        return {"code": 9999, "data": [], "message": "找不到此系统名称"}

    def insert_system(self, systemName, systemPath, creator):
        """
        添加系统名称
        :param systemName: 系统名称
        :param systemPath: 系统地址
        :param creator: 创建者id
        :return:
        """
        result = self.select_system(systemName=systemName)
        if result['code'] == 9999:
            response = self.config.insert_system(systemName=systemName, systemPath=systemPath, userId=creator)
            if response:
                results = self.select_system(systemName=systemName)
                return {"code": 1000, "data": results['data'], "message": "添加成功"}
            return {"code": 9999, "data": [], "message": "添加失败,请重新添加"}
        return {"code": 9999, "data": result['data'], "message": "系统名称已存在"}
