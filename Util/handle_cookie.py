# coding = utf-8
# 1、获取cookie
# 2、写入cookie
# 3、是否携带
import os
import sys
path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)
from Util.handle_json import read_json, write_value
from Util.handle_path import cookie_dir


def get_cookie_value(cookie_key):
    """
    获取cookie
    :param cookie_key:
    :return:
    """
    data = read_json(cookie_dir)
    return data[cookie_key]


def write_cookie(data, cookie_key):
    """
    写入cookie
    :param data:
    :param cookie_key:
    :return:
    """
    data1 = read_json(cookie_dir)
    data1[cookie_key] = data
    write_value(data1)


if __name__ == '__main__':
    data = {
        "cookie": "2222"
    }
    print(get_cookie_value("web"))
    write_cookie(data, "web")
