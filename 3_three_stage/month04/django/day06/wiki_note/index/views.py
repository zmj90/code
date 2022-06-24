from django.shortcuts import render


# Create your views here.
def index_view(request):
    # dict1 = request.GET
    # print(dict1)
    # print(request.GET["c"])
    print(request.GET.get("c"))
    return render(request, "index/index.html")


def home_view(request):
    username = request.session["username"]
    return render(request, "index/home.html", locals())