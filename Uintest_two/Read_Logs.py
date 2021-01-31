from Unittest_Two.ReadPath import GetPath
import ddt
'''

读取logs 内容

殷腾飞

2021-01-31
'''
path = GetPath() + "/result/logs"


def ReadLogs(path):

    with open(path, "r") as f:
        return f.read()


# ret = ReadLogs(path)

