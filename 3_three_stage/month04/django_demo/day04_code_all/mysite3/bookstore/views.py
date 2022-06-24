from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Book

# Create your views here.

def all_book(request):

    all_book = Book.objects.filter(is_active=True)
    #print(all_book)

    return render(request, 'bookstore/all_book.html', locals())

def update_book(request, book_id):

    #获取指定id的数据
    try:
        book = Book.objects.get(id=book_id)
    except Exception as e:
        print('error is %s'%(e))
        return HttpResponse('---当前书籍不存在---')

    if request.method == 'GET':
        return render(request, 'bookstore/update_book.html', locals())

    elif request.method == 'POST':
        #处理数据
        price = request.POST['price']
        market_price = request.POST['market_price']

        book.price = price
        book.market_price = market_price

        book.save()

        return HttpResponseRedirect('/bookstore/all_book')


def delete_book(request, book_id):

    try:
        book = Book.objects.get(id=book_id, is_active=True)
    except Exception as e:
        print('del error is %s'%(e))
        return HttpResponse('---The book is not found')

    book.is_active = False
    book.save()
    return HttpResponseRedirect('/bookstore/all_book')


