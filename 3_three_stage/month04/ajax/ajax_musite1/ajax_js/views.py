from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json


# Create your views here.
def test_xhr(request):
    return render(request, "ajax_js/test_xhr.html")


def test_get(request):
    return render(request, "ajax_js/test_get.html")


def test_get_server(request):
    return HttpResponse("<h1>hello world</h1>")


def test_jquery_get(request):
    return render(request, "ajax_js/test_jquery_get.html")


def test_json(request):
    return render(request, "ajax_js/test_json.html")


def test_make_json_str(request):
    d = [{"uname": "qwe", "age": 30},
         {"unmae": "asd", "age": 29}
         ]
    return JsonResponse(d, safe=False)
