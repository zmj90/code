import time
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(100)
def test_cache(request):

    time.sleep(3)
    t1 = time.time()

    #局部缓存 books = Book.objects.all()
    # cache.set('key', books)

    return HttpResponse('t1 %s'%(t1))


def test_mw(request):

    print('---view do--')

    return HttpResponse('test mw')