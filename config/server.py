"""
@author: hao.ling
@Date: 2020/7/24 10:54 下午
@Annotation: 服务端配置
"""
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from database.user import User

db = SQLAlchemy()

user = User()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:12345678@localhost:3306/testPlatform"
    db.init_app(app)
    create_tables(app)
    user.set_user_id()
    register_blueprints(app)
    return app


def register_blueprints(app):
    from api import api

    CORS(api, supports_credentials=True)
    app.register_blueprint(api, url_prefix='/api')


def create_tables(app):
    from model import users, configurations, testcases, coverage, testreport

    db.create_all(app=app)
