from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


def test_base(request):

    lst = ['Jack', 'Tom']

    print(11111111)
    print(reverse('pag', args=[300]))

    return render(request, 'base.html', locals())

def test_music(request):

    return render(request, 'music.html')

def test_pagen(request, num):

    return HttpResponse('test pagen is ok')

def test_static(request):

    return render(request, 'test_static.html')

