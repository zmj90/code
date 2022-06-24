from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view),
    path('enter/', views.enter_email_view),
    path('send/', views.send_email_view),
    path('verif/',views.verif_email_view)
]