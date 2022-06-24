from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=11, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50, verbose_name='邮箱')
    phone = models.CharField(max_length=11, verbose_name='手机')
    isActive = models.BooleanField(default=False, verbose_name='激活状态')
    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return str(self.id)