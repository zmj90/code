from django.http import HttpResponse
from django.shortcuts import render

POST_HTML = '''
<form method='post' action="/test_post?a=100&b=200">
    姓名:<input type="text" name="username"> 
    <input type='submit' value='登陆'>
</form>
'''

def test_post(request):

    if request.method == 'GET':
        #返回页面
        return HttpResponse(POST_HTML)
    elif request.method == 'POST':
        #处理post提交过来的数据
        a = request.GET['a']
        print('a is %s'%(a))
        username = request.POST['username']
        return HttpResponse('username is %s'%(username))



def test_get(request):

    #test_get?a=100&c=200
    #print(request.GET['d'])
    #print(request.GET.get('d'))

    #test_get?a=100&c=200&a=300&d=400
    print(dict(request.GET))
    print(request.GET.getlist('a'))

    return HttpResponse('---test get is ok---')


def test_page(request):
    #方案1
    # from django.template import loader
    # t = loader.get_template('page.html')
    # html = t.render()
    # return HttpResponse(html)

    #方案2
    from django.shortcuts import render
    return render(request, 'page.html',{'name':'guoxiaonao'})



def test_html(request):

    dic = {}
    dic['int'] = 3
    dic['str'] = 'guoxiaonao'
    dic['lst'] = ['Jack', 'Lily', 'Tom']
    #dic['lst'] = []
    dic['zidian'] = {'name':'wangweichao', 'age':63}
    dic['say_hi'] = say_hi
    dic['class_obj'] = Dog()

    # dic['script'] = '<script>alert(11)</script>'
    dic['script'] = '<div><script>alert(11)</script></div>'

    return render(request, 'test_html.html', dic)


def say_hi():
    return 'Hi everyone~'

class Dog:
    def say(self):
        return 'wangwangha'


def mycal(request):

    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        #计算数据
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']
        if not x or not y:
            return HttpResponse('Please give me a number')
        #文本框空提交? text文本框空提交， name存在，值为''
        #文本框提交数据的数据类型? str

        x = int(x)
        y = int(y)
        result = 0
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            result = x / y

        return render(request, 'mycal.html', locals())




















