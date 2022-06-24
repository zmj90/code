from django.db import models

# Create your models here.
# 用户表
class UserProfile(models.Model):
    username = models.CharField(max_length=11, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50, verbose_name='邮箱')
    isActive = models.BooleanField(default=False, verbose_name='激活状态')
    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return str(self.id)

# 微博用户表
class WeiboUser(models.Model):
    user = models.OneToOneField(UserProfile, verbose_name=u'用户id', null=True,on_delete=models.CASCADE)
    uid = models.CharField(verbose_name=u'微博uid', max_length=10, db_index=True, unique=True)
    access_token = models.CharField(verbose_name=u'微博授权密钥', max_length=32, db_index=True)

    class Meta:
        db_table = 'weibouser'
        verbose_name = '微博用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uid

# 商品表
class SKU(models.Model):
    name = models.CharField(max_length=50, verbose_name='SKU名称')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    stock = models.IntegerField(default=0, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    comments = models.IntegerField(default=0, verbose_name='评价数')
    is_launched = models.BooleanField(default=True, verbose_name='是否上架销售')
    class Meta:
        db_table = 'DDSC_SKU'
        verbose_name = 'SKU表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)


status_choices = (
    (1,"待付款"),
    (2,"待发货"),
    (3,"待收货"),
    (4,"订单完成"),
)
# 订单表
class OrderInfo(models.Model):
    order_id = models.CharField(max_length=64, primary_key=True, verbose_name="订单号")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="下单用户")
    total_count = models.IntegerField(default=1, verbose_name="商品总数")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总金额")
    class Meta:
        db_table = "tb_order_info"
        verbose_name = '订单基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id
# 订单商品表
class OrderGoods(models.Model):
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE, verbose_name="订单")
    sku = models.ForeignKey(SKU, on_delete=models.CASCADE, verbose_name="订单商品")
    count = models.IntegerField(default=1, verbose_name="数量")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")
    class Meta:
        db_table = "tb_order_goods"
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name
# 学生表
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='学生名')
    class_room = models.CharField(max_length=100, verbose_name='班级')
    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)
# 课程表 
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    students = models.ManyToManyField(Student)
    class Meta:
        db_table = 'Course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)