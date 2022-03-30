import sys
import os
path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)

from configparser import ConfigParser
from Util.handle_path import conf_dir


class HandleConfig(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = conf_dir
conf = HandleConfig(file_path)

if __name__ == '__main__':
    conf = HandleConfig("nmb.ini")
    conf.get("log", "name")
