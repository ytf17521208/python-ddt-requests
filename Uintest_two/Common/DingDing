import time
import hmac
import urllib
import hashlib
import base64
from urllib import parse
from dingtalkchatbot.chatbot import DingtalkChatbot
from Unittest_Two.ReadPath import GetPath
from Unittest_Two.Read_logs import ReadLogs
from Unittest_Two.ReadConfig import Ding_Config
path = GetPath() + "/result/logs"
log = ReadLogs(path)
'''
用于钉钉推送消息

殷腾飞

2021-01-31
'''


class DING(object):

    def getSIGN(self):
        timestamp = str(round(time.time() * 1000))
        urlToken = eval(Ding_Config("Token"))
        secret = eval(Ding_Config("secret"))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

        SignMessage = urlToken + "&timestamp=" + timestamp + "&sign=" + sign
        return SignMessage

    def chu_shi(self):
        self.getSIGN()
        SignMessage = self.getSIGN()
        self.xiaoDing = DingtalkChatbot(SignMessage)  # 初始化机器人

    def tsy(self):
        self.chu_shi()
        self.xiaoDing.send_text(log, is_at_all=False)


if __name__ == "__main__":
    DING().tsy()
