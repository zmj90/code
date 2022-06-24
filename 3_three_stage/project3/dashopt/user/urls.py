from django.urls import path
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/v1/users/activation
    path("activation", views.active_view),
    path("<str:username>/address", views.AddressView.as_view()),
    # path("<str:username>")
    path("weibo/authorization", views.weibo_url_view),
    path("weibo/users", views.WeiboUserView.as_view())
]
