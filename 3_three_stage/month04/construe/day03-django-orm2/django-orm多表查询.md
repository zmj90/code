# django-orm多表查询

## 1.表关系关联

常用的表关联方式有三种:

- 一对一映射
  - 如: 一个身份证对应一个人

- 一对多映射
  - 如: 一个班级可以有多个学生
- 多对多映射
  - 如: 一个学生可以报多个课程，一个课程可以有多个学生学习

## 2.一对一表关系映射示例:

- 一对一是表示现实事物间存在的一对一的对应关系。
- 如:一个用户只可关联一个微博用户

```python
class UserProfile(BaseModel):
    username = models.CharField(max_length=11, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50, verbose_name='邮箱')
    isActive = models.BooleanField(default=False, verbose_name='激活状态')
    
    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return str(self.id)
    
class WeiboUser(BaseModel):
    user = models.OneToOneField(UserProfile, verbose_name=u'用户id', null=True)
    uid = models.CharField(verbose_name=u'微博uid', max_length=10, db_index=True, unique=True)

    class Meta:
        db_table = 'weibouser'
        verbose_name = '微博用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.weibo_id
```

- 查询练习:

```python
# 通过userprofile查找weibouser的uid
# 通过weibouser查询userprofile的email
```

## 3.一对多表关系映射示例:

- 一对多是表示现实事物间存在的一对多的对应关系。
- 如:一张订单中有多个商品，一个订单商品可以被多个订单拥有

```python
class SKU(models.Model):
    name = models.CharField(max_length=50, verbose_name='SKU名称')
    caption = models.CharField(max_length=100, verbose_name='副标题')
    SPU_ID = models.ForeignKey(SPU, on_delete=models.CASCADE, verbose_name='商品')
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

class OrderInfo(BaseModel):
    """订单信息"""
    order_id = models.CharField(max_length=64, primary_key=True, verbose_name="订单号")
    user = modelos.ForeignKey(UserPrfile, related_name='orders', on_delete=models.PROTECT, verbose_name="下单用户")
    address = models.ForeignKey(Address, on_delete=models.PROTECT, verbose_name="收货地址")
    total_count = models.IntegerField(default=1, verbose_name="商品总数")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="商品总金额")
    freight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="运费")
    pay_method = models.SmallIntegerField(default=1, verbose_name="支付方式")

    # 1-待发货，2-待支付，3-待收货，
    status = models.SmallIntegerField(verbose_name="订单状态",choices=status_choices)

    class Meta:
        db_table = "tb_order_info"
        verbose_name = '订单基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.order_id
    
class OrderGoods(BaseModel):
    order = models.ForeignKey(OrderInfo, related_name='skus', on_delete=models.CASCADE, verbose_name="订单")
    sku = models.ForeignKey(SKU, on_delete=models.PROTECT, verbose_name="订单商品")
    count = models.IntegerField(default=1, verbose_name="数量")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="单价")
    class Meta:
        db_table = "tb_order_goods"
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sku.name
```

查询练习:

```python
# 通过order.id查询出所有的ordergoods的价格
```

### 4.多对多表关系映射

- 多对多表达对象之间多对多复杂关系，
- 如: 一个学生可以选修多门课，一门课可以被多个学生选修

```python
class Student(models.Model):
    name = models.CharField(max_length=50, verbose_name='学生名')
    class_room = models.CharField(max_length=100, verbose_name='班级')
    class Meta:
        db_table = 'student'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)
    
class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    models.ManyToManyField(Student)
    class Meta:
        db_table = 'Course'
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.id, self.name)
```

查询练习:

```python
# 通过student查询出选修的所有课程
```

## 5.练习题

```python
# 查询出订单2019111118050001购买者的邮箱
# 查看文武双全买了那些商品，打印商品名
# 查询出订单2015111118050003中的商品库存还剩多少
# 查询出订单2019111118050001中价格最便宜的商品价格
# 查询出张三选修了那些课程
```

