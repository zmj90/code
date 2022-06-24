from django.http import HttpResponse,HttpResponseRedirect


def page_2003_view(request):

    html = '<h1>这是第一个页面</h1>'
    #302
    return HttpResponseRedirect('/')
    #return HttpResponse(html)

def index_view(request):

    return HttpResponse('这是首页')

def page1_view(request):

    return HttpResponse('这是page1')

def pagen_view(request, pag):

    print(type(pag))

    html = '这是 page %s !!'%(pag)
    return HttpResponse(html)

def cal_view(request,num1, op, num2):

    #re_path时 传入的参数均为字符串类型
    num1 = int(num1)
    num2 = int(num2)

    if not op in ['sub', 'add', 'mul']:
        return HttpResponse('Your op is wrong !!')

    res = 0
    if op == 'add':
        res = num1 + num2
    elif op == 'sub':
        res = num1 - num2
    elif op == 'mul':
        res = num1 * num2

    return HttpResponse('result is %s'%(res))

def birthday_view(request, y , m, d):

    print(111111111)
    print(request.path_info)
    print(request.method)
    print(request.get_full_path())
    print(request.META)

    return HttpResponse('生日:%s年%s月%s日'%(y,m,d))











