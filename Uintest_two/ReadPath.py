import os
'''
return path

获取当前文件的路径，并返回

殷腾飞

2021-01-31
'''


def GetPath():

    getpath = os.path.split(os.path.realpath(__file__))[0]

    return getpath
