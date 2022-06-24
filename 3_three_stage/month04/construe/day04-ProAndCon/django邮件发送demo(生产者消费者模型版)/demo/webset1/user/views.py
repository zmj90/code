from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile
import random
# Create your views here.
# 登录页面响应
def login_view(request):
    return render(request,'login.html') 

# 验证邮箱页面
def enter_email_view(request):
    return render(request,'enter_email.html')


import redis
r=redis.Redis(host='localhost', port=6379,db=1,decode_responses=True)
# 发送邮件
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
        mails = '%s_%s_%s'%('sendEmail',email_code,user_email)
        r.lpush('mails',mails)
        # 发送邮件
        # from django.core import mail
        # mail.send_mail(
        #             '忘记密码验证',  #标题
        #             "验证码为:%06d" %email_code,  # 消息内容
        #             '1411147737@qq.com',  # 发送者[当前配置邮箱]
        #             recipient_list=[user_email],  # 接收者邮件列表
        #             )
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
