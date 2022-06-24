import base64
import random

from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json

from django.views import View

from .models import UserProfile, Address, WeiboProfile
import hashlib
from dtoken.views import make_token
from django.core.cache import cache
from django.core.mail import send_mail
from .tasks import asyn_send_active_email
from utils.logging_dec import logging_check
from django.conf import settings
from urllib.parse import urlencode
import requests


#10100 - 10199 异常状态码

# Create your views here.
def users(request):

    json_str = request.body
    json_obj = json.loads(json_str)
    #{'uname': 'guoxiaonao', 'password': '123456', 'phone': '13488873110', 'email': '250919354@qq.com', 'carts': None}
    username = json_obj['uname']
    password = json_obj['password']
    phone = json_obj['phone']
    email = json_obj['email']
    #检查参数
    #检查用户名是否可用
    old_users = UserProfile.objects.filter(username=username)
    if old_users:
        result = {'code':10100, 'error': 'The username is already existed !'}
        return JsonResponse(result)
    #创建用户 UserProfile创建数据

    m = hashlib.md5()
    m.update(password.encode())
    password_m = m.hexdigest()
    try:
        user = UserProfile.objects.create(username=username,password=password_m,phone=phone,email=email)
    except Exception as e:
        print('---user create error is')
        print(e)
        result = {'code': 10101, 'error': 'The username is already existed !'}
        return JsonResponse(result)

    #签发jwt token(一天)
    token = make_token(username)

    #激活邮件发送
    #生成四位随机数，将随机数存入redis
    #生成邮件内容 “欢迎注册达达电商，点击《链接》激活”
    try:
        code = "%d" % random.randint(1000, 9999)
        code_str = '%s_%s'%(code, username)
        b64_code = base64.urlsafe_b64encode(code_str.encode()).decode()
        cache.set("email_active_%s"%(username), code, 3600*24*3)
        #生成链接
        verify_url = 'http://127.0.0.1:7000/dadashop/templates/active.html?code=%s'%(b64_code)
        #发送邮件
        #send_active_email(email, verify_url)

        asyn_send_active_email.delay(email, verify_url)
        #.....
    except Exception as e:
        print('----send active email error is %s'%(e))

    return JsonResponse({'code':200,'username':username, 'data':{'token':token.decode()}, 'carts_count':0})



def send_active_email(email_address, verify_url):

    subject = '达达t商城激活邮件'
    html_message = '''
    尊敬的用户您好，请点击激活链接进行激活,
    <a href="%s" target="_blank">点击此处</a>
    '''%(verify_url)

    res = send_mail(subject,'','572708691@qq.com',[email_address],html_message=html_message)
    return res


def active_view(request):
    #获取前端转发的code
    #校验code
    #code合法 更新用户的is_active
    #删除redis中对应的key
    code = request.GET.get('code')
    if not code:
        return JsonResponse({'code':10102, 'error':'not code'})
    code_str = base64.urlsafe_b64decode(code.encode()).decode()

    random_code, username = code_str.split('_')

    old_code = cache.get("email_active_%s"%(username))
    if not old_code:
        return JsonResponse({'code':10103, 'error':'The code is error'})

    if old_code != random_code:
        return JsonResponse({'code':10104, 'error':'The code is error'})

    try:
        user = UserProfile.objects.get(username=username, is_active=False)
    except Exception as e:
        print('active error is %s'%(e))
        return JsonResponse({'code': 10105, 'error': 'The username is error'})

    user.is_active = True
    user.save()

    cache.delete("email_active_%s"%(username))

    return JsonResponse({'code':200, 'data':'OK'})


#FBV function base view
def address_view(request):

    if request.method == 'GET':
        #获取地址
        pass

    elif request.method == 'POST':
        #创建地址
        pass


#CBV class base view
# 按需定义 要使用的method 对应的方法
# 若接收到未定义的动作请求，视图类返回 405响应

class AddressView(View):

    @logging_check
    def get(self, request, username):
        #/v1/users/<username>/address
        '''
        {
        'id':123456, # 地址id
        'address':'广东省深圳市龙华区嘉熙业广场1155室'， # 地址
        'receiver’：’达内科技‘， # 收货人
        'receiver_mobile‘：'12345678901', # 联系电话
        'tag':'家'，# 地址标签
        'postcode':'722494',  #
        'is_default':"True",
        }
        '''
        all_address = Address.objects.filter(user_profile=request.myuser, is_active=True)

        address_list = []
        for addr in all_address:
            addr_data = {}
            addr_data['id'] = addr.id
            addr_data['address'] = addr.address
            addr_data['receiver'] = addr.receiver
            addr_data['receiver_mobile'] = addr.receiver_mobile
            addr_data['tag'] = addr.tag
            addr_data['postcode'] = addr.postcode
            addr_data['is_default'] = addr.is_default
            address_list.append(addr_data)

        return JsonResponse({'code':200, 'addresslist':address_list})


    @logging_check
    def post(self, request, username):
        # /v1/users/<username>/address

        '''
        {
  'receiver':'小王'，
  ‘receiver_phone’:'18667018590',
  'address':'北京市东城区珠市口大街珍贝大厦2楼',
  'postcode':'722405',
  'tag':'公司'
}
        '''
        json_str = request.body
        json_obj = json.loads(json_str)
        receiver = json_obj['receiver']
        receiver_phone = json_obj['receiver_phone']
        address = json_obj['address']
        postcode = json_obj['postcode']
        tag = json_obj['tag']

        user = request.myuser
        old_address = Address.objects.filter(user_profile=user,is_active=True)
        is_default = False
        if not old_address:
            is_default = True

        Address.objects.create(
            user_profile=user,
            receiver=receiver,
            address=address,
            receiver_mobile=receiver_phone,
            postcode=postcode,
            tag=tag,
            is_default=is_default
        )

        return JsonResponse({'code':200, 'data':'新增地址成功！'})

    # def put(self, request):
    #     # /v1/users/<username>/address/<address_id>
    #     return JsonResponse
    #
    # def delete(self, request):
    #     # /v1/users/<username>/address/<address_id>
    #     return JsonResponse




def weibo_url_view(request):

    #https://api.weibo.com/oauth2/authorize?client_id=YOUR_CLIENT_ID&response_type=code&redirect_uri=YOUR_REGISTERED_REDIRECT_URI
    weibo_url = 'https://api.weibo.com/oauth2/authorize'

    params = {
        'client_id': settings.WEIBO_APP_KEY,
        'response_type': 'code',
        'redirect_uri': settings.WEIBO_REDIRECT_URI
    }

    url = weibo_url + '?' + urlencode(params)

    return JsonResponse({'code':200, 'oauth_url':url})



class WeiboUserView(View):

    def get(self, request):

        code = request.GET.get('code')
        if not code:
            return JsonResponse({'code': 10106, 'error':'Please give me code'})

        token_url = 'https://api.weibo.com/oauth2/access_token'
        #发送Post请求

        req_data = {
            'client_id': settings.WEIBO_APP_KEY,
            'client_secret': settings.WEIBO_APP_SECRET,
            'grant_type': 'authorization_code',
            'redirect_uri': settings.WEIBO_REDIRECT_URI,
            'code': code
        }

        response = requests.post(token_url, data=req_data)
        if response.status_code == 200:
            json_data = json.loads(response.text)
        else:
            print(response.status_code)
            return JsonResponse({'code':10107, 'error':'The weibo server is busy'})

        if json_data.get('error'):
            print(json_data['error'])
            return JsonResponse({'code': 10108, 'error': 'The weibo server is busy'})

        print('-----success get token----')
        print(json_data)

        weibo_uid = json_data['uid']
        access_token = json_data['access_token']

        try:
            weibo_user = WeiboProfile.objects.get(wuid=weibo_uid)
        except Exception as e:
            #该微博账号第一次来
            WeiboProfile.objects.create(access_token=access_token,wuid=weibo_uid)
            data = {
                'code': 201,
                'uid': weibo_uid
            }
            return JsonResponse(data)

        else:
            #检查 是否绑定注册过
            user = weibo_user.user_profile
            if user:
                #之前绑定过 - 走正常登录流程
                username = user.username
                token = make_token(username)
                return JsonResponse({'code':200, 'username':username, 'token': token.decode()})

            else:
                #未绑定
                data = {
                    'code':201,
                    'uid': weibo_uid
                }
                return JsonResponse(data)



    def post(self, request):

        json_str = request.body
        json_obj = json.loads(json_str)

        #{"uid":"1861495121","username":"guoxiao8","password":"123456","phone":"13488873110","email":"572708691@qq.com"}
        wuid = json_obj['uid']
        username = json_obj['username']
        password = json_obj['password']
        phone = json_obj['phone']
        email = json_obj['email']

        m = hashlib.md5()
        m.update(password.encode())

        try:
            with transaction.atomic():
                # 生成一个 UserProfile
                user = UserProfile.objects.create(username=username,password=m.hexdigest(), email=email, phone=phone)
                # update 给wuid对应的 WeiboProfile 对象 绑定 外键
                weibo_user = WeiboProfile.objects.get(wuid=wuid)
                weibo_user.user_profile = user
                weibo_user.save()
        except Exception as e:
            print('---bind weibouser error is %s'%(e))
            return JsonResponse({'code':10109 , 'error': 'The database is error'})

        token = make_token(username)
        return JsonResponse({'code':200, 'username':username, 'token':token.decode()})












