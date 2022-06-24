# django邮件服务-生产者消费者模型版

## 1.忘记密码业务流程

![](images\忘记密码流程1.png)

## 2.代码实现-前端:

![](images\前端页面.png)

代码:

略.....

# 3.代码实现-后端:

### 3.1开通qq邮箱POP3服务

开通流程:

1.申请QQ号用QQ号登陆QQ邮箱并修改设置

2.用申请到的QQ号和密码登陆到 <https://mail.qq.com/>

3.修改 `QQ邮箱->设置->帐户->“POP3/IMAP......服务”`设置Django服务器端的.

![](images\SMTP服务开启png.png)

### 3.2django-settings.py配置

```python
# 发送邮件设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # 固定写法
EMAIL_HOST = 'smtp.qq.com' # 腾讯QQ邮箱 SMTP 服务器地址
EMAIL_PORT = 25  # SMTP服务的端口号
EMAIL_HOST_USER = 'xxxx@qq.com'  # 发送邮件的QQ邮箱
EMAIL_HOST_PASSWORD = '******'  # 在QQ邮箱->设置->帐户->“POP3/IMAP......服务” 里得到的在第三方登录QQ邮箱授权码
```

### 3.3 views.py中代码

```python
from django.shortcuts import render
import redis
r=redis.Redis(host='localhost', port=6379,db=1,decode_responses=True)
# 发送邮件
def send_email_view(request):
   if request.method == "POST":
       # 获取邮箱号
        user_email = request.POST.get('user_email')
        # 获取user
        try:
            user = UserProfile.objects.get(useremail=user_email)
        except:
            return HttpResponse('该邮箱尚未注册')
        # 生成验证码
        email_code = random.randint(0, 999999)
        # 存入redis留做验证
        r.setex("email_code_%s" % user_email, 10 * 60, email_code)
        # 发送邮件
        from django.core import mail
        mail.send_mail(
                    '忘记密码验证',  #标题
                    "验证码为:%06d" %email_code,  # 消息内容
                    '1411147737@qq.com',  # 发送者[当前配置邮箱]
                    recipient_list=[user_email],  # 接收者邮件列表
                    )
        return render(request, 'verif_email.html', {'email':user_email})
# 验证邮件
def verif_email_view(request):
    if request.method == "POST":
        verif_code = request.POST.get('verif_code')
        user_email = request.POST.get('email')
        user_code = r.get('email_code_%s'%user_email)
        if user_code == verif_code:
            return HttpResponse('验证成功,请输入新密码xxxx')
        else:
            return HttpResponse('邮箱验证失败')

```

## 4.优化

问题点：

由于django与SMTP交互过程中前端出现阻塞，用户体验不好

解决思路:

生产者消费者模型--解耦合

## 5.代码实现

### 5.1 views.py中

```python
from django.shortcuts import render
# 发送邮件
import redis
r=redis.Redis(host='localhost', port=6379,db=1,decode_responses=True)
def send_email_view(request):
   if request.method == "POST":
       # 获取邮箱号
        user_email = request.POST.get('user_email')
        print(user_email)
        # 获取user
        try:
            user = UserProfile.objects.get(useremail=user_email)
        except:
            return HttpResponse('该邮箱尚未注册')
        # 生成验证码
        email_code = random.randint(0, 999999)
        # 存入redis留做验证
        r.setex("email_code_%s" % user_email, 10 * 60, email_code)
        
        # 发送邮件
        # from django.core import mail
        # mail.send_mail(
        #            '忘记密码验证',  #标题
        #            "验证码为:%06d" %email_code,  # 消息内容
        #            '1411147737@qq.com',  # 发送者[当前配置邮箱]
        #            recipient_list=[user_email],  # 接收者邮件列表
        #            )
        
        
        mails = '%s_%s_%s'%('sendEmail',email_code,user_email)
        r.lpush('mails',mails)
        
        return render(request, 'verif_email.html', {'email':user_email})
# 验证邮件
def verif_email_view(request):
    if request.method == "POST":
        verif_code = request.POST.get('verif_code')
        user_email = request.POST.get('email')
        user_code = r.get('email_code_%s'%user_email)
        if user_code == verif_code:
            return HttpResponse('验证成功,请输入新密码xxxx')
        else:
            return HttpResponse('邮箱验证失败')
```

### 5.2 consumer_worker.py中:

```python
import time
import redis
import os
from django.core import mail
import redis
r=redis.Redis(host='localhost', port=6379,db=1,decode_responses=True)
# django环境的settings文件
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
r=redis.Redis(host='localhost', port=6379,db=1,decode_responses=True)
def work():
    while True:
        mail_ = r.brpop("mails",20*60)
        mails = mail_[1].split('_')
        # 判断业务类型
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
    work()
```
