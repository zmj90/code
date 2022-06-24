from django.db import models

# Create your models here.
class UserProfile(models.Model):

    username = models.CharField(max_length=11, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    #刚注册的用户 需要在激活邮件内 激活后 方可使用用户功能
    is_active = models.BooleanField(default=False, verbose_name='是否激活')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'user_user_profile'




class Address(models.Model):

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    receiver = models.CharField(verbose_name='收件人', max_length=10)
    address = models.CharField(max_length=100, verbose_name='用户地址')
    postcode = models.CharField(verbose_name='邮编', max_length=6)
    receiver_mobile = models.CharField(verbose_name='手机号', max_length=11)
    tag = models.CharField(verbose_name='标签', max_length=10)
    is_active = models.BooleanField(verbose_name='是否活跃', default=True)
    is_default = models.BooleanField(verbose_name='是否为默认地址',default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    def __str__(self):

        return "%s_%s_%s_%s_%s"%(self.id, self.receiver, self.address, self.is_default, self.receiver_mobile)




class WeiboProfile(models.Model):

    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE,null=True)
    wuid = models.CharField(verbose_name='微博uid', max_length=10, unique=True)
    access_token = models.CharField(verbose_name='权限令牌', max_length=32)

    class Meta:
        db_table = 'user_weibo_profile'















