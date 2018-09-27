from flask import Blueprint

__author__ = 'lipeng'
__time__ = '2018/9/27'

web = Blueprint('web', __name__)
# print(str(id(web))+'启动')

from app.web import book



