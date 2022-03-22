import os
import sys
import time

path = os.getcwd()
base_path = os.path.split(path)[0]
sys.path.append(path)

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
conf_dir = os.path.join(base_path, "config")

# 页面截图路径
screenshot_dir = os.path.join(base_path, "Outputs", "screenshots")
