import re
from Unittest_Two.Common.Port_request import Port
from Unittest_Two.ReadConfig import headers_config
'''
return headers

设置的请求头

殷腾飞

2021-01-31
'''


def heads(value=None):

    new = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "48",
            "Content-type": "application/json",
            "Host": "120.27.251.168:9099",
            "Origin": "http://127.0.0.1:9099",
            "Referer": "http://127.0.0.1:9099/",
            "source": "wmdn_pc",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36",
            "Authorization": value
        }
    return new


def __ret():
    post = Port().Mall_port(headers_config("url"), headers_config("data"), heads())
    return_token = re.findall(r'"accessToken": "(.+?)"', post)
    return return_token[0]


'''
返回配置好的请求头

return headers

'''


def return_head():

    return heads(__ret())


# print(return_head())
