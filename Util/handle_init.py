# coding =utf-8
import sys
import os
path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(base_path)
sys.path.append(path)
from base.my_logger import logger
import configparser


class HandleInit:

    def load_ini(self):
        """
        加载ini文件
        :return:
        """
        file_path = base_path + "/config/server.ini"
        cf = configparser.ConfigParser()
        # 获取ini文件，encoding="utf-8-sig"解决中文乱码
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    def get_value(self, key, node=None):
        """
        获取ini里面的value
        """
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            logger.error("获取 {} 的value失败".format(key))
            data = None
        return data


hi = HandleInit()
