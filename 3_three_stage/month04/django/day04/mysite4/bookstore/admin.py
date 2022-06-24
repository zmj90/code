from django.contrib import admin
from .models import *


# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'market_price', "pub"]
    list_display_links = ['title']
    list_filter = ['pub']
    search_fields = ['title']
    list_editable = ['market_price']


admin.site.register(Book, BookManager)


class AuthorManager(admin.ModelAdmin):
    list_display = ["id", "name", "age", "email"]


admin.site.register(Author, AuthorManager)