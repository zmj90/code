from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField("作家姓名", max_length=10)

    def __str__(self):
        return f"name:{self.name}"


class Wife(models.Model):
    name = models.CharField("妻子", max_length=10)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"name:{self.name},author:{self.author}"
