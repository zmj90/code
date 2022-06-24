from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book
import json


# Create your views here.
def get_templates(request):
    return render(request, 'shop.html')


def get_data(request):
    if request.method == "GET":
        # 1. 拿到所有的图书数据.
        books = Book.objects.all()
        datas = ''
        for book in books:
            data = "%s_%s_%s_%s_%s" % (
            book.title, book.describe, str(book.price), 'http://127.0.0.1:8000/media/' + str(book.picture),
            str(book.publisher_date))
            datas += data
            datas += '|'
        datas = datas[0:-1]
        return HttpResponse(datas)



# Book.objects.create(title="python",
#                     describe="人生苦短，我学Python",
#                     price=100,
#                     publisher_date="2020-5-21"
#                     )