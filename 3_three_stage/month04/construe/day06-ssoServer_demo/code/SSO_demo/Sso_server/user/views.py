from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.conf import settings
from .models import UserProfile
import time
# Create your views here.
def make_token(username, expire=3600 * 24):
    # 官方jwt / 自定义jwt
    import jwt
    key = '1234567'
    now = time.time()
    payload = {'username': username, 'exp': int(now + expire)}
    return jwt.encode(payload, key, algorithm='HS256')

# 登录视图
def login(request):
    if request.method == 'GET':
        # 获取子服务器ID
        app_server_id = request.GET.get('app_server_id')
        # 响应登录页面
        return render(request,'login.html',{'app_server_id':app_server_id})
    # 用户提交用户名密码,做登录认证，签发token
    if request.method == 'POST':
        json_str = request.body
        if not json_str:
            result = {'code': 102, 'error': 'Please give me json'}
            return JsonResponse(result)
        json_obj = json.loads(json_str)
        username = json_obj.get('username')
        password = json_obj.get('password')
        if not username:
            result = {'code':103, 'error': 'Please give me username'}
            return JsonResponse(result)
        if not password:
            result = {'code':104, 'error': 'Please give me password'}
            return JsonResponse(result)

        #####校验数据#####
        user = UserProfile.objects.filter(username=username)
        if not user:
            result = {'code':105, 'error': 'username or password is wrong !! '}
            return JsonResponse(result)

        user = user[0]
        if password != user.password:
            result = {'code': 106, 'error': 'username or password is wrong'}
            return JsonResponse(result)
        #make token
        token = make_token(username)
        result = {'code':200, 'username':username, 'data':{'token':token.decode()}}
        return JsonResponse(result)


def verif(request):
    import jwt
    token = request.GET.get('sso_token')
    if not token:
        result = {'code':403, 'error':'Please login'}
        return JsonResponse(result)
    try:
        res = jwt.decode(token, settings.TOKEN_KEY)
    except Exception as e:
        print('jwt decode error is %s'%(e))
        result = {'code':403, 'error':'Please login'}
        return JsonResponse(result)

    except jwt.ExpiredSignatureError:
        #token过期
        result = {'code':403, 'error':'Please login'}
        return JsonResponse(result)

    username = res['username']
    user = UserProfile.objects.get(username=username)
    if not user:
        result = {'code':208, 'error':u'用户名不存在'}
        return JsonResponse(result)
    result = {'code':200,'data':{'username':user.username,'uid':user.id}}
    return JsonResponse(result)