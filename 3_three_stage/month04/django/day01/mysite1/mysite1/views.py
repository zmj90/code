from django.http import HttpResponse, HttpResponseRedirect


def page_view(request):
    html = "<h1>这是我的首页</h1>"
    return HttpResponse(html)
    # return HttpResponseRedirect('https://www.baidu.com')


def page_1_view(request):
    html = "<h1>这是编号为1的网页</h1>"
    return HttpResponse(html)


def page_2_view(request):
    html = "<h1>这是编号为2的网页</h1>"
    return HttpResponse(html)


def pagen_view(request, pag):
    html = f"<h1>这是编号为{pag}的网页</h1>"
    return HttpResponse(html)


# def calculate_view(request, n1, symbol, n2):
#     result = None
#     if symbol == "add":
#         result = n1 + n2
#     elif symbol == "sub":
#         result = n1 - n2
#     elif symbol == "mul":
#         result = n1 * n2
#     return HttpResponse(result)


# def cal_view(request, x, op, y):
#     result = None
#     if symbol == "add":
#         result = n1 + n2
#     elif symbol == "sub":
#         result = n1 - n2
#     elif symbol == "mul":
#         result = n1 * n2
#     return HttpResponse(result)


def date1_view(request, year, month, day):
    return HttpResponse(f"生日为: {year}年{month}月{day}日")


def date2_view(request, month, day, year):
    return HttpResponse(f"生日为: {year}年{month}月{day}日")


