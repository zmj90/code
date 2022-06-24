from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=20, unique=True)
    desc = models.CharField("描述", max_length=200, default="")

    def __str__(self):
        return f"username:{self.username}, desc:{self.desc}"
