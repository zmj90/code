from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def check_login(fn):
    def wrap(request, *args, **kwargs):
        #逻辑位置
        if 'username' not in request.session or 'uid' not in request.session:
            #检查Cookies
            c_username = request.COOKIES.get('username')
            c_uid = request.COOKIES.get('uid')
            if not c_username or not c_uid:
                return HttpResponseRedirect('/user/login')
            else:
                #回写session
                request.session['username'] = c_username
                request.session['uid'] = c_uid
        return fn(request, *args, **kwargs)
    return wrap

@check_login
def add_view(request):

    return HttpResponse('可以添加笔记啦')