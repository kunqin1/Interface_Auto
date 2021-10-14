import sys
import null as null
import requests

from Util.handle_excel import excel_data
from Util.handle_json import read_json
bath_path = 'D:\\Reflection'
sys.path.append(bath_path)


def get_header_value(header_key):
    header = read_json("/config/header.json")
    # data1 = json.loads(data)
    return header[header_key]


if __name__ == '__main__':
    rows = excel_data.get_rows()
    for i in range(rows - 1):
        data = excel_data.get_rows_value(i + 2)
        header_id = data[6]
        print(header_id)
        url = "http://localhost:8080/data/insert"
        data = {
             "ip": "qinkun255",
             "service": "domain",
             "magnification": null,
             "country": null,
             "province": null,
             "city": null
        }
        headers = get_header_value(header_id)
        # header = json.loads(str(headers))
        print(headers)
        print(type(headers))
        res = requests.post(url, data, headers).text
        print(res)
        # print(res)
