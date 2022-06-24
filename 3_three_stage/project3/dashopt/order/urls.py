from django.urls import path

from . import views



urlpatterns = [
    path("<str:username>/advance", views.AdvanceViews.as_view()),
    path("<str:username>", views.OrderInfoView.as_view()),
]