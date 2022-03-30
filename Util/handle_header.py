import os
import sys

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)
from base.my_logger import logger
from Util.handle_json import read_json
from Util.handle_path import header_dir


def get_header_value(header_key):
    try:
        header = read_json(header_dir)
        # data1 = json.loads(data)
        return header[header_key]
    except:
        logger.error("获取 {} 的header".format(header_key))
