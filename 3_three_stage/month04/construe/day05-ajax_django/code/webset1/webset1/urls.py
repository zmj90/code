"""webset1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
Examples:
Function views
    1. Add an import:  from my_app import views
Class-based views
    1. Add an import:  from other_app.views import Home
Including another URLconf
    1. Import the include() function: from django.urls import url, include
"""
from django.urls import path,include,re_path
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
