from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/note/add
    path('add', views.add_view)

]