from django.db import models

# Create your models here.
class Publisher(models.Model):
    #一
    name = models.CharField('出版社名', max_length=10)

class Book(models.Model):
    #多
    title = models.CharField('书名', max_length=10)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
