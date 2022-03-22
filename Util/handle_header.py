import os
import sys
from my_logger import logger
from Util.handle_json import read_json

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)


def get_header_value(header_key):
    try:
        header = read_json("/config/header.json")
        # data1 = json.loads(data)
        return header[header_key]
    except:
        logger.error("获取 {} 的header".format(header_key))
