"""
@author: hao.ling
@Date: 2020/8/15 3:00 下午
@Annotation: 配置中心信息表结构
"""
from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey

from config.server import db


class Environment(db.Model):
    # 环境配置表
    __tableName__ = "environment"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="环境配置id")
    env_name = Column(String(64), nullable=False, comment="环境配置名称")
    env_path = Column(String(125), nullable=False, comment="域名")
    status = Column(Boolean, server_default="0", nullable=False, comment="0:生效,1:无效")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")


class System(db.Model):
    # 系统配置表
    __tableName__ = "system"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="系统配置id")
    system_name = Column(String(64), nullable=False, comment="系统名称")
    system_path = Column(String(128), nullable=False, comment="系统路径")
    status = Column(Boolean, server_default="0", nullable=False, comment="0:生效,1:无效")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")


class Database(db.Model):
    # 数据库配置表
    __tableName__ = "database"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="数据库配置id")
    db_name = Column(String(64), nullable=False, comment="数据库名称")
    db_ip = Column(String(64), nullable=False, comment="数据库地址")
    db_port = Column(Integer(), nullable=False, comment="数据库名称")
    db_username = Column(String(64), nullable=False, comment="数据库用户名")
    db_password = Column(String(64), nullable=False, comment="数据库密码")
    status = Column(Boolean, server_default="0", nullable=False, comment="0:生效,1:无效")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
