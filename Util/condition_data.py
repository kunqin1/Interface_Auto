# coding=utf-8
import json
import sys
import os
import jsonpath

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)
from Util.handle_excel import excel_data
from base.my_logger import logger
from jsonpath_rw import parse


def split_data(data):
    """
    拆分单元格数据
    """
    replace_key = []
    case_id = []
    rule_data = []
    # for item in data:
    # case_id = data.split(">")[0]
    # rule_data = data.split(">")[1]
    # return case_id, rule_data
    for item in data:
        id = item.split(">")[0]
        rule = item.split(">")[1]
        replace_key = item.split(">")[-1]
        case_id.append(id)
        rule_data.append(rule)
    return case_id, rule_data


def depend_data(data):
    """
    获取依赖结果集
    """
    # case_id = split_data(data)[0]
    # row_number = excel_data.get_rows_number(case_id)
    # data = excel_data.get_cell(row_number, 14)
    # return data
    datas = []
    case_ids = split_data(data)[0]
    # print(case_ids)
    for item in case_ids:
        row_number = excel_data.get_rows_number(item)
        data = excel_data.get_cell(row_number, 14)
        datas.append(data)
        json.dumps(datas)
    # print("返回结果集%s" % datas)
    return datas


def get_depend_data1(res_data, key):
    """
    获取依赖字段
    """
    # res_data = json.loads(res_data)
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    return [math.value for math in madle][0]


def get_depend_data(data):
    """
    获取依赖数据
    """
    rule_data = []
    try:
        res_data = depend_data(data)
        # print("数据：{}".format(res_data))
        rule_data = split_data(data)[1]
        return res_data, rule_data
    except:
        logger.error("获取 {} 的依赖原始数据失败".format(rule_data))


def get_data(data):
    datas = []
    try:
        res_datas = get_depend_data(data)[0]
        keys = get_depend_data(data)[1]
        for i in range(len(keys)):
            data1 = json.loads(res_datas[i])
            key = keys[i]
            json_exe = parse(key)
            madle = json_exe.find(data1)
            a = [math.value for math in madle][0]
            datas.append(a)
        return datas
    except:
        logger.error("获取 {} 关联数据失败".format(datas))


if __name__ == '__main__':
    data = ["case_001>resultOBJ.managementDataList[0].ip", "case_002>password"]
    # depend_data(data)
    get_data(data)
