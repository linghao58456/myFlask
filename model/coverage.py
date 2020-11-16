from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, func, ForeignKey

from config.server import db


class coverage(db.Model):
    """覆盖率"""
    __tableName__ = "coverage"

    id = Column(Integer, primary_key=True, autoincrement=True, comment="覆盖率id")
    coverage_name = Column(String(64), nullable=False, comment="覆盖率名称")
    coverage_value = Column(String(64), nullable=False, comment="覆盖率值")
    coverage_script = Column(Integer, ForeignKey("interface.id"), nullable=False, comment="覆盖率脚本")
    remark = Column(String(255), nullable=True, comment="备注信息")
    status = Column(Boolean, server_default="0", nullable=False, comment="0:生效,1:无效")
    creatorId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="创建者id")
    modifyId = Column(Integer, ForeignKey("users.user_id"), nullable=False, comment="修改者id")
    create_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, comment="创建时间")
    modify_time = Column(TIMESTAMP, server_default=func.now(), nullable=False, onupdate=func.now(), comment="修改时间")
