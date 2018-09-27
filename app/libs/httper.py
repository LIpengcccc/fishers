__author__ = 'lipeng'
__time__ = '2018/9/26'

# 两种方式发送Http请求
# 根据状态码判断,增加代码健壮性
# urllib 极为难用
# requests 推荐


from urllib import request
from urllib.parse import quote

import requests
from flask import json


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # if r.status_code == 200:
        #     if return_json:
        #         # 返回json
        #         return r.json()
        #     else:
        #         # 返回普通字符串
        #         return r.text
        # r 是requests对此次http请求的封装
        # restful 返回的结果必须是json格式的
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

    # 简化代码的写法,1.三元表达式 2.if return
    # if return 处理一种特例 return视为函数的终结,结束函数的思维分支
    # 封装成对象是可扩展的
    @staticmethod
    def get_with_request(url, json_return=True):
        # quote编码
        url = quote(url, safe='/:?+&')
        # req = request.Request(url, headers=headers)
        try:
            with request.urlopen(url) as r:
                result_str = r.read()
                result_str = str(result_str, encoding='utf-8')
            if json_return:
                return json.loads(result_str)
            else:
                return result_str
        except OSError as e:
            # 处理404,对于外部的数据，如果出现异常，最好不要抛出来，而是应该默认值处理
            print(e)
            if json_return:
                return {}
            else:
                return None

# python2 存在新式类,加(object)
