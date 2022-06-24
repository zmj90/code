from django.urls import path
from . import views


urlpatterns = [path("detail/<int:user_id>", views.detail),
               path("update/<int:user_id>", views.user_update)
               ]
