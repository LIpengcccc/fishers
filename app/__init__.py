__author__ = 'lipeng'
__time__ = '2018/9/27'

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register(app)
    return app


def register(app):
    # 注册蓝图到app上
    from app.web.book import web
    app.register_blueprint(web)
