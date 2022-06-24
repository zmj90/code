import csv
import os
import time

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
#导入settings
from django.conf import settings
from test_upload.models import Content

@cache_page(100)
def test_cache(request):

    time.sleep(3)
    t1 = time.time()

    #局部缓存 books = Book.objects.all()
    # cache.set('key', books)

    return HttpResponse('t1 %s'%(t1))


def test_mw(request):

    print('---view do--')

    return HttpResponse('test mw')

def test_csrf(request):
    if request.method == 'GET':
        return render(request, 'test_csrf.html')
    elif request.method == 'POST':
        return HttpResponse('post is ok')


def test_page(request):
    # /test_page?page=3
    bks = ['a', 'b', 'c', 'd', 'e']
    paginator = Paginator(bks, 2)

    cur_page = request.GET.get('page', 1)  # 得到默认的当前页
    page = paginator.page(cur_page)

    return render(request, 'test_page.html', locals())

def test_csv(request):
    #修改ct值，添加特殊响应头
    response = HttpResponse(content_type='text/csv')
    #浏览器遇到如下响应头，弹出 另存为 框
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    #book.objects.values('id','title')
    all_book = [{'id':1, 'title':'python1'},{'id':2, 'title':'python2'}]
    #生成csv写入对象
    writer = csv.writer(response)
    writer.writerow(['id', 'title'])
    for book in all_book:
        writer.writerow([book['id'], book['title']])

    return response

@csrf_exempt
def test_upload(request):

    if request.method == 'GET':
        return render(request, 'test_upload.html')

    elif request.method == 'POST':
        #方案1
        # title = request.POST['title']
        # a_file = request.FILES['myfile']
        # print('title is %s'%(title))
        # #int(time.time()) + a_file.name    hello.py
        # filename = os.path.join(settings.MEDIA_ROOT, a_file.name)
        # with open(filename, 'wb') as f:
        #     data = a_file.file.read()
        #     f.write(data)


        #方案2  orm
        title = request.POST['title']
        a_file = request.FILES['myfile']
        Content.objects.create(desc=title, myfile=a_file)

        return HttpResponse('上传成功: %s'%(a_file.name))






