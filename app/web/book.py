from flask import jsonify,request

from app.form.book import SearchForm
from . import web
print(str(id(web))+'开始')
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook

__author__ = 'lipeng'
__time__ = '2018/9/26'

@web.route("/book/search")
def search():
    """

    :param q: 普通关键字 isbn
    :param page:
    :return:
    """
    # app.add_url_rule()
    # Request Response 包含所有的请求信息
    form = SearchForm(request.args)
    if form.validate():
        # a = request.args.to_dict()
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == "isbn":
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q)
        return jsonify(result)
    else:
        return jsonify(form.errors)
