from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import redis


# Create your views here.
r = redis.Redis(host="127.0.0.1", port=6379, db=0, password="123456")


def detail(request, user_id):
    cache_key = f"user:{user_id}"
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        new_data = {k.decode():v.decode() for k,v in data.items()}
        username = new_data["username"]
        desc = new_data["desc"]
        html = f"cache username:{username}  desc:{desc}"
        return HttpResponse(html)
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse("no user")
    username = user.username
    desc = user.desc
    html = f"username:{username}  desc:{desc}"
    r.hmset(cache_key,{"username":username, "desc":desc})
    r.expire(cache_key, 10)
    return HttpResponse(html)


def user_update(request, user_id):
    # /user/update/1?desc=qwe
    desc = request.GET.get("desc", "")
    try:
        user = User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse("no user")
    user.desc = desc
    user.save()
    cache_key = f"user:{user}"
    r.delete(cache_key)
    return HttpResponse("update")