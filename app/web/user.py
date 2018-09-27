__author__ = 'lipeng'
__time__ = '2018/9/27'

from . import web


@web.route('/url')
def login():
    return 'bye bye'
