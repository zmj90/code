from django.db import models


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField('用户名', max_length=11, unique=True)
    password = models.CharField('密码', max_length=32)
    email = models.EmailField('邮箱')
    phone = models.CharField('手机号', max_length=11)
    is_active = models.BooleanField('是否激活', default=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        db_table = 'user_user_profile'


class Address(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    receiver = models.CharField("收件人", max_length=10)
    address = models.CharField("用户地址", max_length=100)
    postcode = models.CharField("邮编", max_length=6)
    receiver_mobile = models.CharField("手机号", max_length=11)
    tag = models.CharField("标签", max_length=10)
    is_active = models.BooleanField("是否活跃", default=True)
    is_default = models.BooleanField("是否为默认地址", default=False)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return f"{self.receiver}_{self.address}_{self.id}_{self.is_default}_{self.receiver_mobile}"


class WeiboProfile(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    wuid = models.CharField("微博uid", max_length=10, unique=True)
    access_token = models.CharField("权限令牌", max_length=32)

    class Meta:
        db_table = "user_weibo_profile"
