from django.urls import path
from . import views


urlpatterns = [path("test_xhr", views.test_xhr),
               path("test_get", views.test_get),
               path("xhr_get_server", views.test_get_server),
               path("test_jquery_get", views.test_jquery_get),
               path("test_json", views.test_json),
               path("test_make_json_str", views.test_make_json_str)
               ]