import requests
import json
'''
封装的请求接口模块

殷腾飞

2021-01-31
'''


class Port(object):

    def Mall_port(self, url, data, head):
        try:
            post = requests.post(url=url, data=data, headers=head).json()
            rest = json.dumps(post, ensure_ascii=False, sort_keys=True, indent=2)
            return rest
        except Exception as w:
            raise ValueError("接口请求失败！", w)


if __name__ == "__main__":
    Port().Mall_port(url="", data="", head="")



