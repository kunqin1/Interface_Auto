# coding=utf-8

import HTMLTestRunner
import sys
from base.baserequest import request
from Util.handle_excel import excel_data
from Util.handle_json import get_value
from Util.handle_result import handle_result_json
from Util.handle_cookie import get_cookie_value
from Util.handle_data import GetData
from Util.handle_header import get_header_value

# print(sys.path[2])
base_path = 'D:\\Reflection'
sys.path.append(base_path)


# print(base_path)
# sys.path.extend('D:\\Reflection')


class Runmain:

    def run_case(self):

        rows = excel_data.get_rows()
        for i in range(rows - 1):
            cookie = None
            get_cookie = None
            headers = None
            data = excel_data.get_rows_value(i + 2)
            header_id = data[6]
            cookieMethod = GetData.get_cookie(data)
            method = GetData.get_method(data)
            # print("------>"+ method)
            url = GetData.get_url(data)
            # data2 = data[5]
            result_method = GetData.get_result_method(data)
            data1 = GetData.get_data2(data)
            # 将字符串转化成字典
            is_headers = GetData.get_header(data)

            if is_headers == "yes":
                headers = get_header_value(header_id)
            if cookieMethod == "yes":
                # 根据key选择携带的cookie
                cookie = get_cookie_value('web')
            if cookieMethod == 'write':
                get_cookie = {"is_cookie": "app"}
            # 转到 baserequest 发送请求class
            res = request.send_main(method, url, data1, headers, get_cookie, cookie)
            # print(data[0])
            # print(res)
            if result_method == 'json':
                result = get_value(url, "/config/result.json")
                result1 = handle_result_json(res, result)
                if result1:
                    print(str(data[0]) + ":" + "pass")
                else:
                    print(str(data[0]) + ":" + "false" + str(res))

            if result_method == 'errcode':
                if "Bad Request" == res['error']:
                    print(str(data[0]) + ":" + "pass")
                else:
                    print(str(data[0]) + ":" + "false" + str(res))
            if result_method == 'mcd':
                if 'success' in res:

                    # max_clos=excel_data.get_sheet_data().max_column
                    if ('True' in str(res['success']) and "成功" in res['message']) or (
                            'False' in str(res['success']) and "失败" in res['message']):
                        print(str(data[0]) + ":" + "pass")
                    # excel_data.excel_write_data(i+2, max_clos, "pass")
                    else:
                        print(str(data[0]) + ":" + "false" + str(res))
                    # excel_data.excel_write_data(i+2, max_clos, "false")
                else:
                    print(str(data[0]) + ":" + "false" + str(res))


if __name__ == '__main__':
    run = Runmain()
    file_path = base_path+'/report/report.html'
    with open(file_path,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="this is test", description="test")
        runner.run()

