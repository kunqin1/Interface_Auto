# coding =utf -8
import sys
from Util.handle_excel import excel_data
import json

base_path = 'D:\\Reflection'
sys.path.append(base_path)


class get_data():
    """
    读取excel中method,url,data,header,result_method数据
    """

    def get_method(self, data=None):
        method = data[7]
        return method

    def get_url(self, data=None):
        url = data[6]
        return url

    def get_data2(self, data=None):
        data2 = data[5]
        data1 = data2.encode("utf-8")
        return data1

    def get_result_method(self, data=None):
        result_method = data[9]
        return result_method

    def get_header(self, data=None):
        header = data[4]
        # print(header)
        # headers = json.loads(header)
        return header

    def get_cookie(self, data=None):
        cookie=data[8]
        return cookie


GetData = get_data()
if __name__ == '__main__':
    GetData = get_data()
    GetData.get_method()
    GetData.get_data2()
