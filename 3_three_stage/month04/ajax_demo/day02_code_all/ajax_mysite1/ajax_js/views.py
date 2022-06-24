# from django.http import HttpResponse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import User
import json


# Create your views here.
def test_xhr(request):
    return render(request, 'ajax_js/test_xhr.html')


def test_get(request):
    print(request.GET)
    print(type(request.body))
    print(request.body)
    # return render(request, 'ajax_js/test_get.html')
    return render(request, 'ajax_js/test_jq_get.html')


def test_get_server(request):
    print(request.GET)
    print(type(request.body))
    print(request.body)
    return HttpResponse('---hahahaha---')


def test_get_user(request):
    # 获取用户数据
    s = 'username_age&username1_age_1'
    pass


def test_json(request):
    return render(request, 'ajax_js/test_json.html')


def test_make_json_str(request):
    d = [{'uname': 'wwc', 'age': 18}, {'uname': 'gxn', 'age': 19}]
    return JsonResponse(d, safe=False)


def get_user(request):
    return render(request, 'ajax_js/get_user.html')


def get_user_server(request):
    # 接收ajax请求，返回json 字符串
    users = User.objects.all()
    u_list = [{"username": u.username, "age": u.age} for u in users]
    # for u in users:
    #     d = {}
    #     d['username'] = u.username
    #     d['age'] = u.age
    #     u_list.append(d)
    return JsonResponse(u_list, safe=False)

    # from django.core import serializers
    # users = User.objects.all()
    # json_str = serializers.serialize('json', users)
    # return HttpResponse(json_str, content_type='application/json')


def test_post(request):
    return render(request, 'ajax_js/test_post.html')


def test_post_server(request):
    print(request.POST)
    # <QueryDict: {'uname': ['qwe'], 'csrfmiddlewaretoken': ['e8q0yiJNZiMalqdI8JcXzPahpzxnSy0OgGdIUF9Rse1y0IwGnlZFdDwZyvFz0Clv']}>
    print(request.body)
    name = request.POST.get("uname")
    csrf = request.POST.get("csrfmiddlewaretoken")
    return HttpResponse(f'{name}---post is ok---{csrf}')


def cross_view(request):
    return render(request, 'ajax_js/cross.html')


def cross_server_json(request):

    func = request.GET.get('callback')
    print(func)
    d = {'name': 'guoxiaonao', 'age': 18}
    return HttpResponse(func + "(" + json.dumps(d) + ")")
