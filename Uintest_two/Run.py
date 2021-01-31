import sys
import os
import ddt
import unittest
import re
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Unittest_Two.ReadExcel import get_xls  # 用例模块
from Unittest_Two.Common.Port_request import Port  # 接口请求模块
from Unittest_Two.Return_Headers import return_head  # 请求头模块
from Unittest_Two.Asser.Assertions import Assertions1  # 断言模块
from Unittest_Two.CreateHTML import create  # 生成HTML

xls = get_xls('doLogin.xlsx', 'Sheet1')

'''
使用ddt处理读取的文件中数据，并执行接口请求

殷腾飞

2021-01-31
'''


@ddt.ddt
class mall(unittest.TestCase):

    def setUp(self):
        """
        :return:
        """

        print("----测试开始前准备----")

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    @ddt.data(*xls)
    @ddt.unpack
    def test1(self, url, data, module, case, code, verify):
        try:
            print("测试内容为：%s---%s" % (module, case))
            post = Port().Mall_port(url=url, data=data, head=return_head())
            print(post)
            #  判断返回的  code  是否正确
            return_code = re.findall(r'"code": (.+?),', post)
            Assertions1().Values_Code(int(return_code[0]), int(code))

            #  判断返回的  data  是否正确
            return_message = re.findall(r'"message": "(.+?)"', post)
            if return_message != []:
                Assertions1().Values_Data(return_message[0], verify)
            else:
                print("message值为空！")
        except Exception as s:
            raise ValueError("执行接口失败！", s)


'''
生成HTML、发送邮件、发送叮叮推送消息

'''

create(mall)



