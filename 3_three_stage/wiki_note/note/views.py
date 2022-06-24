from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import *


# Create your views here.
def check_login(fn):
    def wrap(request, *args, **kwargs):
        if "username"  not in request.session or "uid" not in request.session:
            username = request.COOKIES.get("username")
            uid = request.COOKIES.get("uid")
            if not username or not uid:
                return HttpResponseRedirect("/user/login")
            else:
                request.session["username"] = username
                request.session["uid"] = uid
        return fn(request, *args, **kwargs)
    return wrap


@check_login
def list_view(request):
    username = request.session["username"]
    user = User.objects.get(username=username)
    # notes = Note.objects.filter(user=user)
    notes = user.note_set.all()
    return render(request, "note/list_note.html", locals())


@check_login
def add_view(request):
    if request.method == "GET":
        return render(request, "note/add_note.html")
    elif request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        user = User.objects.get(username=request.session["username"])
        user.note_set.create(title=title, content=content)
        return HttpResponseRedirect("/note")


def mod_view(request, num):
    try:
        note = Note.objects.get(id=num)
        # print(note)
    except Exception as e:
        return HttpResponse("no")
    if request.method == "GET":
        return render(request, "note/mod_note.html", locals())
    elif request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        return HttpResponseRedirect("/note")


def del_view(request, num):
    try:
        note = Note.objects.get(id=num)
    except Exception as e:
        return HttpResponse("no")
    note.delete()
    return HttpResponseRedirect("/note")