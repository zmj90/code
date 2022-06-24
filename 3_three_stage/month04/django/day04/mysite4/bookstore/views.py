from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def all_book(request):
    books = Book.objects.filter(is_active=True)
    return render(request, 'bookstore/all_book.html',locals())


def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print(e)
        return HttpResponse('---当前书籍不存在---')
    if request.method == "GET":
        return render(request, "bookstore/update_book.html", locals())
    elif request.method == "POST":
        book.price = request.POST.get("price")
        book.market_price = request.POST.get("market_price")
        book.save()
        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request, delete_id):
    book = Book.objects.get(id=delete_id)
    book.is_active = False
    book.save()
    return HttpResponseRedirect("/bookstore/all_book")


def add_book(request):
    if request.method == "GET":
        return render(request, "bookstore/add_book.html")
    elif request.method == "POST":
        Book.objects.create(title=request.POST.get("title"),
                            pub=request.POST.get("pub"),
                            price=request.POST.get("price"),
                            market_price=request.POST.get("market_price")
                            )
        return HttpResponseRedirect("/bookstore/all_book")