"""
    10100 - 10199 异常状态码
"""
import base64
from random import randint
from django.core.cache import cache
from django.db import transaction
from django.http import JsonResponse
import json
from django.views import View
from .models import *
import hashlib
from dtoken.views import make_token
from .tasks import asyn_send_active_email
from utils.logging_dec import logging_check
from django.conf import settings
from urllib.parse import urlencode
import requests


# Create your views here.
def users(request):
    # 获取数据
    json_str = request.body
    json_obj = json.loads(json_str)
    # print(json_obj)
    # {'uname': 'wwwwww', 'password': '111111', 'phone': '13628387691', 'email': '909600795@qq.com', 'carts': None}
    username = json_obj['uname']
    password = json_obj['password']
    phone = json_obj['phone']
    email = json_obj['email']
    carts = json_obj["carts"]

    # 检查参数
    # 检查用户名是否可用
    old_users = UserProfile.objects.filter(username=username)
    if old_users:
        result = {'code': 10100, 'error': 'The username is already existed !'}
        return JsonResponse(result)

    # 创建用户
    m = hashlib.md5()
    m.update(password.encode())
    password_m = m.hexdigest()
    try:
        user = UserProfile.objects.create(username=username, password=password_m, phone=phone, email=email)
    except Exception as e:
        print('---user create error is')
        print(e)
        result = {'code': 10101, 'error': 'The username is already existed !'}
        return JsonResponse(result)

    # 签发jwt
    token = make_token(username)

    # 激活邮件发送
    try:
        code = f"{randint(1000,9999)}"
        code_str = f"{code}_{username}"
        # print(code_str)
        # 2804_wwwwww
        b64_code = base64.urlsafe_b64encode(code_str.encode()).decode()
        cache.set(f"email_active_{username}", code, 3600*24*3)
        verify_url = f"http://127.0.0.1:7000/dadashop/templates/active.html?code={b64_code}"
        # send_active_email(email, verify_url)
        asyn_send_active_email.delay(email, verify_url)
    except Exception as e:
        print(f"send active emali error is {e}")

    return JsonResponse({'code': 200, 'username': username, 'data': {'token': token.decode()}, 'carts_count': 0})


def active_view(request):
    code = request.GET.get("code")
    if not code:
        return JsonResponse({"code": 10102, "error": "not code"})
    code_str = base64.urlsafe_b64decode(code.encode()).decode()
    random_code, username = code_str.split("_")
    old_code = cache.get(f"email_active_{username}")
    if not old_code:
        return JsonResponse({"code": 10103, "error": "the error is errors"})
    if old_code != random_code:
        return JsonResponse({"code": 10104, "error": "the error is error"})
    try:
        user = UserProfile.objects.get(username=username, is_active=False)
    except Exception as e:
        print(f"active error is {e}")
        return JsonResponse({"code": 10105, "error": "the username is error"})
    user.is_active = True
    user.save()
    cache.delete(f"email_active_{username}")
    return JsonResponse({'code': 200, 'data': 'ok'})


# FBV function base view
def address_view(request):
    if request.method == "GET":
        pass
    elif request.method == "PORT":
        pass


# CBV class base view
class AddressView(View):
    """
        {
      "code":200,
       "addresslist":[
          {
            'id':123456, # 地址id
            'address':'广东省深圳市龙华区嘉熙业广场1155室'， # 地址
            'receiver’：’达内科技‘， # 收货人
            'receiver_mobile‘：'12345678901', # 联系电话
            'tag':'家'，# 地址标签
            'postcode':'722494',  #
            'is_default':"True",
          },
        }
          """
    @logging_check
    def get(self, request, username):
        # 127.0.0.1:8000/v1/users/<username>/address
        if username != request.myuser.username:
            return JsonResponse({"code": 403, "error": "Please login"})
        loging_user = request.myuser

        all_address = Address.objects.filter(user_profile=loging_user, is_active=True)
        address_list = []
        for addr in all_address:
            addr_data = {}
            addr_data["id"] = addr.id
            addr_data["receiver"] = addr.receiver
            addr_data["address"] = addr.address
            addr_data["receiver_mobile"] = addr.receiver_mobile
            addr_data["tag"] = addr.tag
            addr_data["postcode"] = addr.postcode
            addr_data["is_default"] = addr.is_default
            address_list.append(addr_data)

        return JsonResponse({"code": 200, "addresslist": address_list})



    # 405    Method Not Allowed
    # 404    Not Found
    @logging_check
    def post(self, request, username):
        """
        {
  'receiver':'小王'，
  ‘receiver_phone’:'18667018590',
  'address':'北京市东城区珠市口大街珍贝大厦2楼',
  'postcode':'722405',
  'tag':'公司'
}
        """
        json_str = request.body
        json_obj = json.loads(json_str)
        receiver = json_obj["receiver"]
        receiver_phone = json_obj["receiver_phone"]
        address = json_obj["address"]
        postcode = json_obj["postcode"]
        tag = json_obj["tag"]

        user = request.myuser
        old_address = Address.objects.filter(user_profile=user, is_active=True)

        is_default  = False
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



        return JsonResponse({"code": 200, "data": "新增地址成功"})

    # def put(self, request):
    #     return JsonResponse
    #
    # def delete(self,request):
    #     return JsonResponse


def weibo_url_view(request):
    # https://api.weibo.com/oauth2/authorize?client_id=800363476&response_type=code&redirect_uri=YOUR_REGISTERED_REDIRECT_URI

    # url转义
    # https://api.weibo.com/oauth2/authorize?client_id=800363476&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A7000%2Fdadashop%2Ftemplates%2Fcallback.html

    # 微博302跳转至 预留页面
    # http://127.0.0.1:7000/dadashop/templates/callback.html?code=9142af45d3bfbcee1c1baa3e1bcef744

    # 前端 8000 get 转发授权码
    # http://127.0.0.1:8000/v1/users/weibo/users?code=9142af45d3bfbcee1c1baa3e1bcef744
    weibo_url = "https://api.weibo.com/oauth2/authorize"
    params = {
        "client_id": settings.WEIBO_APP_KEY,
        "response_type": "code",
        "redirect_uri": settings.WEIBO_REDIRECT_URI
    }
    url = weibo_url + "?" + urlencode(params)
    return JsonResponse({"code": 200, "oauth_url": url})


class WeiboUserView(View):
    def get(self, request):
        code = request.GET.get("code")
        if not code:
            return JsonResponse({"code": 10106, "error": "Please give me code"})

        token_url = "https://api.weibo.com/oauth2/access_token"
        req_data = {
            "client_id": settings.WEIBO_APP_KEY,
            "client_secret": settings.WEIBO_APP_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": settings.WEIBO_REDIRECT_URI,
            "code": code
        }
        response = requests.post(token_url, data=req_data)
        if response.status_code == 200:
            json_data = json.loads(response.text)
        else:
            print(response.status_code)
            return JsonResponse({"code": 10107, "error": "The sinaserver is busy"})

        if json_data.get("error"):
            return JsonResponse({"code": 10108, "error": "The sinaserver is busy"})

        print("---------------------success get token--------------")
        print(json_data)

# ---------------------success get token--------------
# {'access_token': '2.00eM11YF01GPKs7b4596438507myRd', 'remind_in': '157679999', 'expires_in': 157679999, 'uid': '5087903808', 'isRealName': 'true'}
        weibo_uid = json_data["uid"]
        access_token = json_data["access_token"]
        try:
            weibo_user = WeiboProfile.objects.get(wuid=weibo_uid)
        except Exception as e:
            WeiboProfile.objects.create(access_token=access_token, wuid=weibo_uid)
            data = {
                "code": 201,
                "uid": weibo_uid,
            }
            return JsonResponse(data)
        else:
            user = weibo_user.user_profile
            if user:
                username = user.username
                token = make_token(username)
                return JsonResponse({"code": 200, "username": username, "token": token.decode()})
            else:
                data = {
                    "code": 201,
                    "uid": weibo_uid
                }
                return JsonResponse(data)


    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)

        wuid = json_obj["uid"]
        username = json_obj["username"]
        password = json_obj["password"]
        phone = json_obj["phone"]
        email = json_obj["email"]

        m = hashlib.md5()
        m.update(password.encode())
        # 生成UserProfile
        # update 绑定外键
        # 开事务
        try:
            with transaction.atomic():
                user = UserProfile.objects.create(username=username, password=m.hexdigest(), email=email, phone=phone)
                weibo_user = WeiboProfile.objects.get(wuid=wuid)
                weibo_user.user_profile = user
                weibo_user.save()
        except Exception as e:
            return JsonResponse({"code": 10109, "error":
            "The database is error"})

        token = make_token(username)
        return JsonResponse({"code": 200, "username": username, "token": token.decode()})
