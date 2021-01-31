import os
import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Unittest_Two.Read_logs import ReadLogs
from Unittest_Two.ReadConfig import Email_config
log = ReadLogs("/Users/a123/Desktop/Automation/Unittest_Two/result/logs")
'''
用于发送邮件  QQ

殷腾飞

2021-01-31
'''


class SendEmail(object):
    def __init__(self, file=None, ssl=False, email_host='smtp.qq.com', port=25, ssl_port=465):
        self.file = file  # 附件路径，如果不在当前目录下，要写绝对路径
        self.email_host = email_host  # smtp服务器地址
        self.port = port  # 普通端口
        self.ssl = ssl  # 是否安全链接
        self.ssl_port = ssl_port  # 安全链接端口

    def send_email(self):
        msg = MIMEMultipart()
        # 发送内容的对象
        if self.file:  # 处理附件的
            f_name = os.path.split(self.file)[-1]  # 只取文件名，不取路径
            try:
                f = open(self.file, 'rb').read()
            except Exception as e:
                raise Exception('附件打不开！！！！', e)
            else:
                att = MIMEText(f, "base64", "utf-8")
                att["Content-Type"] = 'application/octet-stream'
                f_name = '=?utf-8?b?' + base64.b64encode(f_name.encode()).decode() + '?='
                # 这里是处理文件名为中文名的，必须这么写
                att["Content-Disposition"] = 'attachment; filename="%s"' % (f_name)
                msg.attach(att)
        msg.attach(MIMEText(log))  # 邮件正文的内容
        msg['Subject'] = "接口自动化测试邮件"  # 邮件主题
        msg['From'] = Email_config("addresser")  # 发送者账号
        msg['To'] = ','.join(Email_config("addressee"))  # 接收者账号列表
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 发送邮件服务器的对象
        self.smtp.login(Email_config("addresser"), Email_config("password"))
        try:
            self.smtp.sendmail(Email_config("addresser"), Email_config("addressee"), msg.as_string())
            pass
        except Exception as e:
            print('出错了。。', e)
        else:
            print('发送成功！')
        self.smtp.quit()


if __name__ == '__main__':
    m = SendEmail(
        file=r'/Unittest_Two/result/logs',
        ssl=True
    )
    m.send_email()
