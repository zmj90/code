from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100,verbose_name='用户名')
    password = models.CharField(max_length=100,verbose_name='密码')
    useremail  = models.EmailField(max_length=19,verbose_name='邮箱')