# coding = utf-8
import sys
import json

base_path = 'D:\\Reflection'
sys.path.append(base_path)


def read_json(file_name=None):
    if file_name is None:
        file_path = base_path + "/Config/user_data.json"
    else:
        file_path = base_path + file_name
    with open(file_path, encoding='UTF-8') as f:
        data = json.load(f)
    return data


#
# "api3/getbanneradvertver2":[
#         {"1006":"token error"}, code：1006  message:token error
#         {"1006":"用户名错误"},
#         {"1006":"密码错误"}
#     ]
# 通过字典中get方法通过code获取message


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
