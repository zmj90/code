from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
import hashlib


# Create your views here.
def reg_view(request):
    if request.method == "GET":
        return render(request, "user/register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")
        if not username:
            return HttpResponse("Please give me username")
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse("用户名已存在")
        if password_1 != password_2:
            return HttpResponse("密码不一样")
        m = hashlib.md5()
        m.update(password_2.encode())
        password_h = m.hexdigest()
        try:
            User.objects.create(username=username, password=password_h)
        except Exception as e:
            print(f"error is {e}")
            return HttpResponse("用户名已存在")
    return render(request, "user/to_login.html")


def login_view(request):
    if request.method == "GET":
        # print(request.session.get("username", "no"))
        if "username" in request.session and "uid" in request.session:
            return HttpResponseRedirect("/index/home")
        username = request.COOKIES.get("username")
        uid = request.COOKIES.get("uid")
        if username and uid:
            request.session["username"] = username
            request.session["uid"] = uid
            return HttpResponseRedirect("/index/home")
        return render(request, "user/login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse("用户名或密码错误")
        m = hashlib.md5()
        m.update(password.encode())
        password_h = m.hexdigest()
        if password_h != old_user.password:
            return HttpResponse("用户名或密码错误")
        request.session["uid"] = old_user.id
        request.session["username"] = username
        resp = HttpResponseRedirect("/index/home")
        if "remember" in request.POST:
            resp.set_cookie("username", username, 3600 * 24 * 3)
            resp.set_cookie("uid", old_user.id, 3600 * 24 * 3)
        return resp


def logout_view(request):
    resp = HttpResponseRedirect("/user/login")
    del request.session["uid"]
    del request.session["username"]
    resp.delete_cookie("uid")
    resp.delete_cookie("username")
    return resp
