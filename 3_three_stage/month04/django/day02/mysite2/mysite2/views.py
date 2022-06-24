from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

POST_HTML = """
<form method='post' action="/test_post">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>"""


def test_post(request):
    if request.method == "GET":
        return HttpResponse(POST_HTML)
    elif request.method == "POST":
        username = request.POST["username"]
        return HttpResponse(f'<h1>{username}</h1>')


def test_get(request):
    # print(request.GET["a"])
    print(request.GET.get("d"))  # None
    return HttpResponse("test get is ok")


def test_page(request):
    t = loader.get_template("page.html")
    html = t.render({"name": "钟马俊"})
    return HttpResponse(html)
    # return render(request, "page.html", {"name": "钟马俊"})


def test_html(request):
    dic = {}
    dic["int"] = 3
    dic["str"] = "zmj"
    dic["lst"] = ["jack", "lily", "tom"]
    dic["say_hi"] = say_hi
    dic["Dog"] = Dog()

    dic["script"] = "<script>alert(11)</script>"
    return render(request, "test.html", dic)


def say_hi():
    return "hello"


class Dog:
    def say(self):
        return "okok"


def test_cal(request):
    if request.method == "GET":
        return render(request, "calculate.html")
    elif request.method == "POST":
        x = request.POST.get("x")
        op = request.POST.get("op")
        y = request.POST.get("y")
        return HttpResponse("ok")


def main(request):
    return render(request, "main.html")


def page1(request):
    return render(request, "page1.html")


def page2(request):
    return render(request, "page2.html")


def page3(request):
    return render(request, "page3.html")