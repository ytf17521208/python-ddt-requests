import os
import configparser
from Unittest_Two.ReadPath import GetPath
'''
拼接链接 获取链接中的内容

return config values

殷腾飞

2021-01-31
'''
path = os.path.join(GetPath(), "config.ini")
# 调用外部的读取配置文件的方法
config = configparser.ConfigParser()
config.read(path, encoding='utf-8')
'''
获取config 中headers中的数据
'''


def headers_config(va):

    value = config.get("HEADERS", va)
    return value


'''
获取 config 中 email 中的数据
'''


def Email_config(va):
    value = config.get("EMAIL", va)
    return value


'''
获取 config 中 叮叮 中的数据

'''


def Ding_Config(va):
    value = config.get("DING", va)
    return value
