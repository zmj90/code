from django.http import HttpResponse


def set_cookies(request):
    resp = HttpResponse("--set-cookies--")
    resp.set_cookie("name", "zmj", 30)
    resp.set_cookie("age", 30, 30)
    return resp


def get_cookies(request):
    value = request.COOKIES.get("name", "no value")
    return HttpResponse(f"the cookies key name value is {value}")


def delete_cookies(request):
    resp = HttpResponse("del cookies")
    resp.delete_cookie("name")
    resp.delete_cookie("age")
    return resp


def set_session(request):
    request.session["name"] = "zmj"
    request.session["age"] = 30
    return HttpResponse("set session")


def get_session(request):
    value = request.session.get("name", "no value")
    age = request.session.get("age", "no age")
    return HttpResponse(f"value:{value}----age:{age}")
