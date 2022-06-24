import time
import redis
import os
from django.core import mail
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
r=redis.Redis(host='localhost', port=6379,db=1,decode_responses=True)
def send_mail_work():
    while True:
        mail_ = r.brpop("mails",20*60)
        mails = mail_[1].split('_')
        if mails[0] == 'sendEmail':
            mail.send_mail(
                        '忘记密码验证',  #标题
                        '验证码:'+mails[1],  # 消息内容
                        '1411147737@qq.com',  # 发送者[当前配置邮箱]
                        recipient_list=[mails[2]],  # 接收者邮件列表
                        )
        else:
            print('其他业务')
if __name__ == '__main__':
    send_mail_work()