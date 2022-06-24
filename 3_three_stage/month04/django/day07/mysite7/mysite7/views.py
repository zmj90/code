import time

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse


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