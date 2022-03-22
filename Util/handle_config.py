import sys
from configparser import ConfigParser
import os

from Util.handle_path import conf_dir

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)


class HandleConfig(ConfigParser):

    def __init__(self, file_path):
        super().__init__()
        self.read(file_path, encoding="utf-8")


file_path = os.path.join(conf_dir, "server.ini")
conf = HandleConfig(file_path)

if __name__ == '__main__':
    conf = HandleConfig("nmb.ini")
    conf.get("log", "name")
