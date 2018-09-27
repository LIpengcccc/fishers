from app import create_app

__author__ = 'lipeng'
__time__ = '2018/9/26'

from flask import Flask


app = create_app()


app = create_app()

if __name__ == '__main__':
    # 生产环境nginx+uwsgi
    app.run(debug=app.config['DEBUG'])
