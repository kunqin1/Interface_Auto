# coding=utf-8
import json
import requests
import sys

from Util.handle_cookie import write_cookie
from Util.handle_init import hi

base_path = 'D:\\Reflection'
sys.path.append(base_path)


# print(base_path)


class baserequest():
    """
    发生post请求
    """

    def send_post(self, url, data, header=None, get_cookie=None, cookie=None):
        response = requests.post(url=url, data=data, headers=header, cookies=cookie)
        if get_cookie is not None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    """
    发送get请求
    """

    def send_get(self, url, data, header=None, get_cookie=None, cookie=None):
        response = requests.post(url=url, data=data, headers=header, cookies=cookie)
        if get_cookie is not None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    """
    发送请求，传递method,url，data参数
    """

    def send_main(self, method, url, data, header=None, get_cookie=None, cookie=None):

        base_host = hi.get_value('host')  # 获取host
        if 'http' not in url:
            url = base_host + url

        if method == 'post':
            res = self.send_post(url, data, header, get_cookie, cookie)
        else:
            res = self.send_get(url, data, header, get_cookie, cookie)

        try:
            res = json.loads(res)
        except:
            print("这是一个text")

        return res


"""
实例化对象
"""
request = baserequest()
if __name__ == '__main__':
    request = baserequest()

    request.send_main('get', '/login', "{'username':'11111'}")
