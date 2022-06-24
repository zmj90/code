from django.urls import path
from . import views

urlpatterns = [
    #http://127.0.0.1:8000/bookstore/all_book
    path('all_book', views.all_book),
    #http://127.0.0.1:8000/bookstore/update_book/<book_id>
    path('update_book/<int:book_id>', views.update_book),
    #http://127.0.0.1:8000/bookstore/delete_book/<book_id>
    path('delete_book/<int:book_id>', views.delete_book)
]