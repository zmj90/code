from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import redis
# Create your views here.
r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='123456')

def user_detail(request, user_id):
    #1,先查缓存
    # 没有： 数据库 -> 数据回写缓存
    # 有： 返回缓存内容
    cache_key = 'user:%s'%(user_id)
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        #{b'username':b'guoxiaonao', b'age':b'20'}
        new_data = {k.decode():v.decode() for k,v in data.items()}
        username = new_data['username']
        age = new_data['age']
        html = 'Cache username is %s age is %s'%(username, age)
        return HttpResponse(html)

    #无缓存时
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        print(e)
        return HttpResponse('--no user')

    username = user.username
    age = user.age
    html = 'username is %s age is %s' % (username, age)
    #更新缓存
    r.hmset(cache_key, {'username':username, 'age':age})
    r.expire(cache_key, 60)
    return HttpResponse(html)


def user_update(request, user_id):

    #/user/update/1?age=30
    age = request.GET.get('age', 0)

    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('--no user')

    user.age = age
    user.save()

    #删除缓存
    cache_key = 'user:%s'%(user_id)
    r.delete(cache_key)

    return HttpResponse('--update is ok--')
































