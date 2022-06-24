from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/ajax_js/test_xhr
    path('test_xhr', views.test_xhr),
    #http://127.0.0.1:8000/ajax_js/test_get
    path('test_get', views.test_get),
    path('xhr_get_server', views.test_get_server)
]
