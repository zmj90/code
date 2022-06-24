from django.urls import path
from . import views


urlpatterns = [path("get_user", views.get_user),
               path("get_user_server", views.get_user_server)
               ]
