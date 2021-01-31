import unittest
import os
from Unittest_Two.ReadPath import GetPath
import Unittest_Two.Common.HTMLTestRunner as HTMLTestRunner
from Unittest_Two.ReadConfig import Email_config
from Unittest_Two.Common.configEmail import SendEmail
from Unittest_Two.Common.DingDing import DING
from Unittest_Two.ReadConfig import Ding_Config
from Unittest_Two.Read_logs import ReadLogs
path = GetPath() + "/result/logs"
log = ReadLogs(path)
'''
生成HTML

殷腾飞

2021-01-31
'''


def create(Dict):
    try:
        suite = unittest.TestSuite()
        loader = unittest.TestLoader()
        suite.addTest(loader.loadTestsFromTestCase(Dict))

        report_dir = os.path.join(GetPath(), "result")
        Html_Name = report_dir + "/" + "report.html"

        with open(Html_Name, "wb+") as file:
            runner = HTMLTestRunner.HTMLTestRunner(file, 2, title="The interface test template",
                                                   description="Please see below the generated report execution results"
                                                               "report")
            runner.run(suite)
    except Exception as e:
        raise ValueError("生成HTML失败！", e)

    if Email_config("on_off") == "on_off":
        m = SendEmail(
            file=r'/Users/a123/Desktop/Automation/Unittest_Two/result/report.html',
            ssl=True,
        )
        m.send_email()
    else:
        raise ValueError("发送邮件开关未打开，请打开邮件开关重新执行！")

    try:
        if Ding_Config("off_on") == str('"off_on"'):
            DING().tsy()
            print("叮叮推送消息已发送！")
        else:
            pass
    except Exception as e:
        raise ValueError("叮叮推送消息发送失败！", e)



