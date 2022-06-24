from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/user/detail/1
    path('detail/<int:user_id>', views.user_detail),
    #http://127.0.0.1:8000/user/update/1
    path('update/<int:user_id>', views.user_update)
]