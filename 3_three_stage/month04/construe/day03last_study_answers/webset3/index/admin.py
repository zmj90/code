from django.contrib import admin
from .models import UserProfile,WeiboUser,SKU,OrderInfo,OrderGoods,Student,Course
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(WeiboUser)
admin.site.register(SKU)
admin.site.register(OrderInfo)
admin.site.register(OrderGoods)
admin.site.register(Student)
admin.site.register(Course)