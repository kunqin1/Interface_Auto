# coding=utf-8
import json
import unittest
import sys
import os
import unittest
from baserequest import request

# headers = {'Content-Type': 'application/json'}
# print(type(headers))
url1 = '/data/delete'


class reflection_case(unittest.TestCase):

    def test_one(self):
        headers = {'Content-Type': 'application/json'}
        # print(type(headers))
        # ensure_ascii = False可以消除json包含中文的乱码问题
        data = {"serviceResourceManagementDtoList":
                    [{'ip': 'kun001', 'service': 'domain'},
                     {'ip': 'kun001', 'service': 'qqqqqq'}
                     ]}
        # print(type(data))
        res = request.send_main('post', url1, data, headers)
        self.assertEqual("操作成功", res['message'])

    def test_add01(self):
        url = '/data/insert'
        headers = {"Content-Type": "application/json"}
        # print(headers)
        print(type(headers))
        # data为字典
        data1 = {
            'ip': 'kun001',
            'service': 'domain',
            'magnification': 20,
            'country': '北京',
            'province': 'jkkl',
            'city': 'jkjkl'
        }
        # 将字典转化为字符串（就是json格式）
        """ print("-----")
        print(type(data1))
        print("-----")
        
        print(data)
        # res1=requests.post(url1,data,headers)
        """
        data = json.dumps(data1)
        res = request.send_main('post', url, data, headers)
        # res=requests.post(url, data=data, json=header)
        print(res)
        self.assertEqual("操作成功", res['message'])

    def test_add02(self):
        headers = {"Content-Type": "application/json"}
        # print(type(headers))
        url = "/data/update"
        data = json.dumps({

            "ip": "ksdjfsk",
            "service": "qqqqqq",
            "magnification": 50,
            "country": None,
            "province": "北京市",
            "city": None,
            "last_update_time": "2020-06-22 17:31:56"
        })
        res = request.send_main('post', url, data, headers)
        print(res)
        self.assertEqual(res['message'], "操作成功")


if __name__ == "__main__":
    unittest.main()
