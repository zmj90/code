from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/ajax_js/test_xhr
    path('test_xhr', views.test_xhr),
    #http://127.0.0.1:8000/ajax_js/test_get
    path('test_get', views.test_get),
    path('xhr_get_server', views.test_get_server),

    path('test_json', views.test_json),
    path('test_make_json_str', views.test_make_json_str),

    path('get_user', views.get_user),
    path('get_user_server', views.get_user_server),

    path('test_post', views.test_post),
    path('test_post_server', views.test_post_server),

    path('test_cross', views.cross_view),
    path('cross_server', views.cross_server_json)

]