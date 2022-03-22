import json
import os
import time
import unittest
import sys
import ddt
import HTMLTestRunner
from Util.condition_data import get_data
from Util.handle_path import reports_dir
from base.baserequest import request
from Util.handle_excel import excel_data
from Util.handle_result import handle_result_json
from Util.handle_cookie import get_cookie_value
from Util.handle_data import GetData
from Util.handle_header import get_header_value

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(base_path)
soure_data = excel_data.get_excel_data()


@ddt.ddt
class TestCase(unittest.TestCase):

    @ddt.data(*soure_data)
    def test_main_case(self, data):
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_run = GetData.get_RunState(data)
        case_id = GetData.get_caseId(data)
        i = excel_data.get_rows_number(case_id)
        if is_run == 'yes':
            is_depend = GetData.get_isDpend(data)
            data1 = json.loads(GetData.get_RQpar(data))
            if is_depend:
                '''
                获取依赖数据
                '''
                depend_key = GetData.get_replace_key(data)
                depend_data = get_data(is_depend)
                data1[depend_key] = depend_data
            # 请求方式
            method = GetData.get_method(data)
            # url
            url = GetData.get_url(data)
            # 根据url获取header
            header_id = GetData.get_url(data)
            # 是否需要携带header
            is_header = GetData.get_header(data)
            # 预期结果方式
            excepect_method = GetData.get_result_method(data)
            # 预期结果
            excepect_result = GetData.get_excepect_result(data)
            # cookie的方式
            cookie_method = GetData.get_cookie(data)
            if cookie_method == 'yes':
                cookie = get_cookie_value('app')
            if cookie_method == 'write':
                '''
                必须是获取到cookie
                '''
                get_cookie = {"is_cookie": "app"}
            if is_header == 'yes':
                header = get_header_value(header_id)

            res = request.send_main(method, url, data1, cookie, get_cookie, header)
            # excel_data.excel_write_data(i, 13, res)
            code = str(res['errorCode'])
            message = res['errorDesc']
            # message+errorcode

            if excepect_method == 'mec':
                config_message = handle_result_json.handle_result(url, code)
                try:
                    self.assertEqual(message, config_message)
                    excel_data.excel_write_data(i, 13, "通过")
                    excel_data.excel_write_data(i, 14, res)
                except Exception as e:
                    excel_data.excel_write_data(i, 13, "失败")
                    raise e
            if excepect_method == 'errcode':
                try:
                    self.assertEqual(excepect_result, code)
                    excel_data.excel_write_data(i, 13, "通过")
                    excel_data.excel_write_data(i, 14, res)
                except Exception as e:
                    excel_data.excel_write_data(i, 13, "失败")
                    raise e
            if excepect_method == 'json':
                if code == 1000:
                    status_str = 'sucess'
                else:
                    status_str = 'error'
                excepect_result = handle_result_json.get_result_json(url, status_str)
                result = handle_result_json(res, excepect_result)
                try:
                    self.assertTrue(result)
                    excel_data.excel_write_data(i, 13, "通过")
                    excel_data.excel_write_data(i, 14, res)
                except Exception as e:
                    excel_data.excel_write_data(i, 13, "失败")
                    raise e


if __name__ == "__main__":
    case_path = base_path + "/Run"
    now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = reports_dir + "/report.html"
    print(report_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test_run_*.py")
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description="this is test")
        runner.run(discover)
