from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def test_xhr(request):
    return render(request, 'ajax_js/test_xhr.html')


def test_get(request):
    # return render(request, 'ajax_js/test_get.html')
    return render(request, 'ajax_js/test_jq_get.html')

def test_get_server(request):

    return HttpResponse('---hahahaha---')


