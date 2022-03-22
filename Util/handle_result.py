import os
import sys
from Util.handle_json import get_value
from deepdiff import DeepDiff

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(base_path)
sys.path.append(path)


def handle_result(url, code):
    """
    根据url获取结果json文件中message
    根据字典中的get(cade)获取message
    :param url: 发送请求的url
    :param code: 返回参数的code
    :return:
    """
    data = get_value(url, "/config/code_message.json")
    if data is not None:
        for i in data:
            message = i.get(str(code))
            if message is not None:
                return message
        return None


def get_result_json(url):
    """
    根据url获取返回数据格式
    :param url:
    :return:
    """
    data = get_value(url, "/config/result.json")
    print(data)


def handle_result_json(dict1, dict2):
    # 传递比较的json格式
    '''
    校验格式
    '''
    # 判断两个是字典
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        dict1 = {"aaa": "AAA", "bbb": "BBBB", "CC": [{"11": "22"}, {"11": "44"}]}
        dict2 = {"aaa": "123", "bbb": "456", "CC": [{"11": "111"}, {"11": "44"}]}
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        # print(type(cmp_dict))
        # 判断返回结果中的key为dictionary_item_added
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False


if __name__ == '__main__':
    # print(handle_result('api3/getbanneradvertver2', "1002"))
    dict1 = {"aaa": "AAA", "bbb": "BBBB", "CC": [{"11": "22"}, {"11": "44"}]}
    dict2 = {"aaa": "123", "bbb": "456", "CC": [{"11": "111"}, {"11": "44"}]}
    # handle_result_json(dict1,dict2)
    get_result_json("/data/insert")
