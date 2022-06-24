from django.db import models


# Create your models here.
class Publisher(models.Model):
    name = models.CharField("出版社", max_length=30)


class Book(models.Model):
    title = models.CharField("书名", max_length=10)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
