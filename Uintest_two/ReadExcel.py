import os
from Unittest_Two.ReadPath import GetPath
# 调用读Excel的第三方库xlrd
from xlrd import open_workbook
'''
return xlsx values

读取文件，并返回内容

殷腾飞

2021-01-31
'''


def get_xls(FileName, filename):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
    csv = []
    # 获取用例文件路径
    xlsPath = os.path.join((GetPath() + "/CaseFile"), FileName)
    file = open_workbook(xlsPath)  # 打开用例Excel
    sheet = file.sheet_by_name(filename)  # 获得打开Excel的sheet
    # 获取这个sheet内容行数
    now = sheet.nrows
    for i in range(now):  # 根据行数做循环
        csv.append(sheet.row_values(i))
    return csv
