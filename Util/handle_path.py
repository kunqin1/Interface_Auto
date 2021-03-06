import os
import sys
import time

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)
sys.path.append(base_path)

now_time = time.strftime("%Y-%m-%d %H-%M-%S")

# 测试用例路径
cases_dir = base_path + "/case/用例.xlsx"

# 测试数据的路径
# datas_dir = os.path.join(base_dir, "TestDatas")

# 测试报告
reports_dir = os.path.join(base_path, "Outputs", "reports")

# 日志的路径
logs_dir = os.path.join(base_path, "Outputs", "logs")

# 配置文件路径
conf_dir = os.path.join(base_path, "config", "server.ini")

# header配置文件路径
header_dir = os.path.join(base_path, "config", "header.json")

# code_message信息配置文件路径
code_dir = os.path.join(base_path, "config", "code_message.json")

# 断言json配置文件路径
json_dir = os.path.join(base_path, "config", "result.json")

# cookie存放配置文件路径
cookie_dir = os.path.join(base_path, "Config", "cookie.json")

# 页面截图路径
screenshot_dir = os.path.join(base_path, "Outputs", "screenshots")

