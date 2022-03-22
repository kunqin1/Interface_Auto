# coding = utf-8
import os
import sys
import json

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(base_path)


def read_json(file_name=None):
    if file_name is None:
        file_path = base_path + "/Config/user_data.json"
    else:
        file_path = base_path + file_name
    with open(file_path, encoding='UTF-8') as f:
        data = json.load(f)
    return data


def get_value(key, file_name):
    data = read_json(file_name)
    return data.get(key)
    # return data[key]


def write_value(data):
    """
    写入cookie的值
    :param data:
    :return:
    """
    data_value = json.dumps(data)
    with open(base_path + "/Config/cookie.json", 'w') as f:
        f.write(data_value)


if __name__ == '__main__':
    print(read_json("/config/result.json"))
    print(get_value("/data/insert", "/config/result.json"))
