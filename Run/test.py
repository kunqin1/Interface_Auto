from Util.handle_path import cases_dir
import xlrd
workbook = xlrd.open_workbook(cases_dir)  # 打开excel文件
Data_sheet = workbook.sheet_by_name('Sheet1')  # 通过名称获取工作簿
rowNum = Data_sheet.nrows  # sheet行数

headers = Data_sheet.row_values(0)  # 获取标题行数据
for i in range(1, rowNum):  # 跳过标题行，从第二行开始取数据
    d = list(zip(headers, Data_sheet.row_values(i)))  # 将标题和每行数据组装成字典,zip将两个列表组合成一个lis
    print(type(d))
    print(d)
