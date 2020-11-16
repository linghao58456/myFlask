from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey

from config.server import db


class functional(db.Model):
    """功能用例"""
    __tableName__ = "functional"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="用例id")
    case_name = Column(String(64), unique=True, nullable=False, comment="用例名称")
    case_des = Column(String(64), nullable=True, comment="用例描述")
    case_pri = Column(Boolean, server_default="1", comment="优先级(0:高，1:中，2:低)")
    case_step = Column(String(255), nullable=False, comment="用例步骤")
    case_front = Column(String(255), nullable=True, comment="前置条件")
    case_expected = Column(String(255), nullable=False, comment="预期结果")
    case_actual = Column(String(255), nullable=False, comment="实际结果")
    remark = Column(String(255), nullable=True, comment="备注信息")
    status = Column(Boolean, server_default="0", nullable=False, comment="0:生效,1:无效")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")


class interface(db.Model):
    """接口用例"""
    __tableName__ = "interface"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="用例id")
    case_name = Column(String(64), unique=True, nullable=False, comment="用例名称")
    case_des = Column(String(255), nullable=True, comment="用例描述")
    case_address = Column(String(64), nullable=False, comment="接口地址")
    case_path = Column(String(255), nullable=False, comment="接口路径")
    case_port = Column(String(64), nullable=False, comment="端口号")
    case_method = Column(Boolean, server_default="0", comment="请求方式(0:get,1:post,2:put,3:delete)")
    case_header = Column(String(255), nullable=True, comment="请求头")
    case_data = Column(String(255), nullable=False, comment="请求参数")
    case_pri = Column(Boolean, server_default="1", comment="优先级(0:高,1:中,2:低)")
    case_expected = Column(String(255), nullable=False, comment="预期结果")
    case_actual = Column(String(255), nullable=False, comment="实际结果")
    remark = Column(String(255), nullable=True, comment="备注信息")
    status = Column(Boolean, server_default="0", nullable=False, comment="0:生效,1:无效")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
