from django.db import models

# Create your models here.
class Book(models.Model):

    title = models.CharField("书名", max_length=10)
    #00000.00
    price = models.DecimalField("定价", max_digits=7,decimal_places=2)
    desc = models.CharField("描述", max_length=30, default='')



