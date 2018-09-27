from app.libs.httper import HTTP

__author__ = 'lipeng'
__time__ = '2018/9/26'


from flask import current_app


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def calculate_start(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    def search_by_keyword(self, keyword, page=1):
        # 请求上下文帮我们把current_app推入到栈中
        url = YuShuBook.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None
