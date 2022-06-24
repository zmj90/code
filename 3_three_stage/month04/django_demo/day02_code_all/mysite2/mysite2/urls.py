"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #http://127.0.0.1:8000/test_get
    path('test_get', views.test_get),
    #http://127.0.0.1:8000/test_post
    path('test_post', views.test_post),
    #http://127.0.0.1:8000/test_page
    path('test_page', views.test_page),
    #http://127.0.0.1:8000/test_html
    path('test_html', views.test_html),
    #http://127.0.0.1:8000/mycal
    path('mycal', views.mycal)

]
