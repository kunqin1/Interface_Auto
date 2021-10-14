# coding = utf-8
# 1、获取cookie
# 2、写入cookie
# 3、是否携带
import sys
import json
from Util.handle_json import get_value, read_json, write_value
bath_path = 'D:\\Reflection'
sys.path.append(bath_path)


def get_cookie_value(cookie_key):
    """
    获取cookie
    :param cookie_key:
    :return:
    """
    data = read_json("/Config/cookie.json")
    return data[cookie_key]


def write_cookie(data, cookie_key):
    """
    写入cookie
    :param data:
    :param cookie_key:
    :return:
    """
    data1 = read_json("/Config/cookie.json")
    data1[cookie_key] = data
    write_value(data1)


if __name__ == '__main__':
    data = {
        "cookie":"2222"
    }
    print(get_cookie_value("web"))
    write_cookie(data, "web")