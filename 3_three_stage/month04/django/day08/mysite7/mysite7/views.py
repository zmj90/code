import os
import time
from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@cache_page(100)
def test_cache(request):
    time.sleep(3)
    t1 = time.time()
    return HttpResponse(f"t1:{t1}")


def test_mw(request):
    print("view")
    return HttpResponse("test_mw")


def test_csrf(request):
    if request.method == "GET":
        return render(request, "test_csrf.html")
    elif request.method == "POST":
        return HttpResponse("post is ok")


def test_page(request):
    bks = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(bks, 2)
    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)
    return render(request, 'test_page.html', locals())


@csrf_exempt
def test_upload(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == "POST":
        a_file = request.FILES['myfile']
        print("上传文件名是:", a_file.name)
        filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        with open(filename, 'wb') as f:
            data = a_file.file.read()
            f.write(data)
        return HttpResponse("接收文件:" + a_file.name + "成功")