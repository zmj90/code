from django.http import JsonResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def get_user(request):
    return render(request, "user/get_user.html")


def get_user_server(request):
    users = User.objects.all()
    list1 = []
    for obj in users:
        d = {}
        d["name"] = obj.username
        d["age"] = obj.age
        list1.append(d)
    print(list1)
    return JsonResponse(list1, safe=False)
