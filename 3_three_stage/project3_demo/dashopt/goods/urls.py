from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [

    path('index', cache_page(600, cache='goods')(views.GoodsIndexView.as_view())),
    path('detail/<int:sku_id>', views.GoodsDetailView.as_view())

]

#删缓存
#缓存中的数据     mysql数据

#cache_page 缓存删除原理
# 独立存储
# 如何触发删除？  admin

