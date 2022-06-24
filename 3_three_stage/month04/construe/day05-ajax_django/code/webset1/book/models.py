from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='书名')
    describe = models.CharField(max_length=300, verbose_name='描述')
    price = models.DecimalField(default=None, verbose_name='单价', max_digits=5, decimal_places=2)
    picture = models.ImageField(verbose_name="图片", default=None)
    publisher_date = models.DateField(verbose_name='出版时间')


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
