import json
import os

import null
import requests
import sys
from my_logger import logger
from requests import utils
from Util.handle_cookie import write_cookie
from Util.handle_init import hi

# 获取当前文件的目录，D:\Interface_Auto\base
path = os.getcwd()
# 把最后的一个目录和前面的目录分开，返回一个元组('D:\\Interface_Auto', 'base')
base_path = os.path.split(path)
base_path = base_path[0]
# 将base——path添加到环境变量中去
sys.path.append(base_path)
path = os.getcwd()


class baserequest():
    """
    发生post请求
    """

    def send_post(self, url, data, header=None, get_cookie=None, cookie=None):
        response = requests.post(url=url, data=data, headers=header, cookies=cookie)
        if get_cookie is not None:
            # 获取cookies的值为CookieJar类型
            cookie_value_jar = response.cookies
            # 使用requests.utils.dict_from_cookiejar转化为字典
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
            logger.error("写入cookies失败")
        res = response.text
        logger.error("获取{}的数据失败".format(url))
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
            logger.error("写入cookies失败")
        res = response.text
        logger.error("获取{}的数据失败".format(url))
        return res

    """
    发送请求，传递method,url，data参数
    """

    def send_main(self, method, url, data, header=None, get_cookie=None, cookie=None):
        base_host = hi.get_value('host')  # 获取host
        if base_host:
            if 'http' not in url:
                url = base_host + url
            if method == 'post':
                res = self.send_post(url, data, header, get_cookie, cookie)
            else:
                res = self.send_get(url, data, header, get_cookie, cookie)
            try:
                res = json.loads(res)
            except:
                logger.info("这是一个text")
            return res
        else:
            logger.error("获取host失败")


"""
实例化对象
"""
request = baserequest()
if __name__ == '__main__':
    request = baserequest()

    request.send_main('get', '/login', "{'username':'11111'}")
