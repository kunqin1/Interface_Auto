# coding =utf -8
import os
import sys
import json
path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)


class get_data():
    """
    读取excel中method,url,data,header,result_method数据
    """

    def get_RunState(self, data=None):
        is_run = data[3]
        return is_run

    def get_caseId(self, data=None):
        caseid = data[0]
        return caseid

    def get_method(self, data=None):
        method = data[6]
        return method

    def get_url(self, data=None):
        url = data[2]
        return url

    def get_RQpar(self, data=None):
        data2 = data[7]
        data1 = data2.encode("utf-8")
        return data1

    def get_result_method(self, data=None):
        result_method = data[10]
        return result_method

    def get_header(self, data=None):
        # 是否需要写的header
        header = data[9]
        return header

    def get_cookie(self, data=None):
        cookie = data[8]
        return cookie

    def get_replace_key(self, data=None):
        """
        获取代替的参数名称
        :param data:
        :return:
        """
        try:
            key = json.loads(data[5])
            return key
        except:
            return None

    def get_isDpend(self, data=None):
        """
        获取前置数据表达式
        :param data:
        :return:
        """
        try:
            is_depend = json.loads(data[4])
            return is_depend
        except:
            return None

    def get_excepect_result(self, data=None):
        """
        获取预期结果的值
        :param data:
        :return:
        """
        excepect_result = data[11]
        return excepect_result


GetData = get_data()
if __name__ == '__main__':
    GetData = get_data()
    GetData.get_method()
