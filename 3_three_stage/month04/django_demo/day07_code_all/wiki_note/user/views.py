from django.http import HttpResponse
from django.shortcuts import render
from .models import User
import hashlib

# Create your views here.
def reg_view(request):

    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        #处理数据
        username = request.POST.get('username')
        password_1 = request.POST.get('password_1')
        password_2 = request.POST.get('password_2')

        if not username:
            return HttpResponse('Please give me username')

        #检查username是否可用
        old_users = User.objects.filter(username=username)
        if old_users:
            return HttpResponse('The username is already existed')

        #密码处理
        #hash算法
        if password_1 != password_2:
            return HttpResponse('The password is not same')
        #hash算法特点
        #1,定长输出 - 无论输入多长/输出长度一定是定长的
        #2,不可逆 - 无法通过hash值计算出明文
        #3,雪崩效益 - 输入变化，则输出一定变化 [文件完整性校验]

        m = hashlib.md5()
        m.update(password_1.encode())
        password_h = m.hexdigest()

        try:
            #并发引起 数据库重复插入的错误
            user = User.objects.create(username=username, password=password_h)
        except Exception as e:
            print('error is %s'%(e))
            return HttpResponse('The username is already existed')

    return HttpResponse('reg is ok')



def login_view(request):

    if request.method == 'GET':
        #优先检查session,如果已登录，显示 '您已登录'
        if 'username' in request.session and 'uid' in request.session:
            return HttpResponse('--您已登录--')
        #检查Cookies
        username = request.COOKIES.get('username')
        uid = request.COOKIES.get('uid')
        if username and uid:
            #[回写session]
            request.session['username'] = username
            request.session['uid'] = uid
            return HttpResponse('--您已登录--')

        return render(request, 'user/login.html')

    elif request.method == 'POST':
        #处理数据
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            old_user = User.objects.get(username=username)
        except Exception as e:
            return HttpResponse('The username or password is wrong~')

        m = hashlib.md5()
        m.update(password.encode())
        password_h = m.hexdigest()

        if password_h != old_user.password:
            return HttpResponse('The username or password is wrong~')

        #存储状态[一天]
        request.session['uid'] = old_user.id
        request.session['username'] = username
        #print(11111111)
        #print(request.POST)

        #判断是否存储Cookies
        resp = HttpResponse('--登录成功--')
        if 'remember' in request.POST:
            resp.set_cookie('username',username,3600*24*3)
            resp.set_cookie('uid', old_user.id, 3600*24*3)

        return resp






        return HttpResponse('---登录成功---')







