from django.db import models

# Create your models here.
class Author(models.Model):

    name = models.CharField('作家姓名', max_length=10)
    #book_set

class Book(models.Model):

    title = models.CharField('书名', max_length=10)
    authors = models.ManyToManyField(Author)



