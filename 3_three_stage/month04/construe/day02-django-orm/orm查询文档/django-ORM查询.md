# django-ORM查询

## 说明:

通過 Entry.objects 的屬性調用查詢接口,例如:

```python
querys = Entry.objects.all()
query = Entry.objects.filter()
```

  queryset是查询集，Django会对查询返回的结果集QerySet进行缓存，这里是为了提高查询效率，也就是说，在你创建一个QuerySet对象的时候，Django并不会立即向数据库发出查询命令，只有在你需要用到这个QuerySet的时候才回去数据库查询

返回QuerySet对象的方法

```django
all()        #返回表中所有数据
filter()     #返回符合条件的数据
exclude()    #返回不符合条件的数据
order_by()   #返回查询结果集进行排序
```

特殊的QuerySet

```django
values() 返回一个可迭代的字典序列
values_list() 返回一个可迭代的元祖序列
```

返回具体对象

```django
get()    #返回满足条件的对象
first()  #返回第一条数据
last()   #返回最后一条数据
```

**queryset的方法**

返回布尔值

```django
exists()   #判断查询的数据是否存在
```

返回数字

```django
count()  #返回查询集中对象的数目
```

## 1.基本查詢操作

语法:

```python
Entry.objects.all()
```

作用:

將Entry實體的所有記錄查詢出來 select * from table;

返回值:

QuerySet 查询结果集list。

## tips:

QuerySet 对象有一个query属性，它可以返回查询方法所用的sql语句.

**只有querySet对象有此方法**

## 2.指定列查询

语法:

```python
Entry.objects.values('列1','列2')
Entry.objects.all().values('列1','列2')
```

作用:

返回的是每个元素为字典的QuerSet 对象

返回值:

QuerySet 會將查詢出來的部分列封裝到字典中,再封裝到列表中

## 3.指定列查询

语法:

```python
Entry.objects.values_list("列1","列2")
```

作用:

返回的是每个元素为元组的QuerSet 对象

返回值:

QuerySet            會將查詢出來的部分列封裝到元組中,再封裝到列表中

## 4.只查詢一條數據出來

语法:

```python
Entry.objects.get()
```

作用:

查詢只能返回一條數據

返回值:

QuerySet            

注意:

該方法只能返回一條數據,查詢結果多餘一條(多个结果)或沒有查詢到結果(0)的話都會拋出異常

## 练习

## 5.根據條件查詢部分行數據

语法:

```python
 Entry.objects.filter(参数)
```

作用:

筛选出与所给筛选条件相匹配的对象，多个条件是and的关系.

返回值:

QuerySet            會將查詢結果封裝到列表裏     

参数:

可以指定多个条件  

## 6.根據條件查詢部分行數據(非等值)

语法:

```python
Entry.objects.filter(屬性__謂詞 = 值)
```

查询谓词:

```shell
__gt     			大于
__gte   			大于等于
__lt      			小于
__lte    			小于等于
__in     			存在于一个list范围内
__startswith    	以...开头
__istartswith   	以...开头忽略大小写
__endswith     		以...结尾
__iendswith    		以...结尾，忽略大小写
__range   			在...范围内
__year      		日期字段的年份
__month   			日期字段的月份
__day        		日期字段的日
__overlap      		集合至少有一个元素重合
__contains     		集合包含
__regex          	匹配正则表达式
```

示例:

```python
# 年龄大于10岁的数据
Entry.objects.filter(age__gt=10)
# 00年出生的老师
Entry.objects.filter(borthday__year='2000')
```

## 7.做不等的條件篩選

语法:

```python
Author.objects.exclude(條件)
```

作用:

筛选出与所给筛选条件不匹配的对象，多个条件是and的关系

示例:

```python
# 不姓郭的老师
Entry.objects.exclude(name__startswith='郭')
```

## 8.排序查詢 

语法:

```
Entry.objects.order_by("列","-列")
```

作用:

默認是升序排序,如果想要降序則在列名前加 - 號即可

返回值:

queryset 对选哪个

## 9.聚合操作

语法:

```python
import django.db.models import Avg,Max,Min
Enrty.objects.aggregate(Avg('age'),Max('age'),Mix('age'))
```

功能:

对筛选的结果进行聚合

返回值:

字典

## 10.分组聚合

语法:

```python
QuerySet.annotate(num=Count('id'))
```

作用:

对筛选的结果进行分组聚合

注意:

如果annotate前写values，则values内的字段即分组条件，得到的结果是一个个字典组成的QuerySet对象

## 11.F查询

语法:

```python
Entry.object.filter(id__gt=F('age'))
```

作用:

F() 的实例可以在查询中引用字段，来比较同一个 model 实例中两个不同字段的值。

说明:

支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。

```python
Entry.object.filter(id__gt=F('age')/2)
```

修改操作也可以使用F函数,比如将每位作者的年龄+1岁

```python
Entry.objects.all().update(age=F("age")+1)
```

## 12.Q查询

作用:

filter() 等方法中的关键字参数查询都是一起进行“AND” 的。 如果你需要执行更复杂的查询（例如OR语句），你可以使用Q对象

你可以组合& 和| 操作符以及使用括号进行分组来编写任意复杂的Q 对象。同时，Q 对象可以使用~ 操作符取反，这允许组合正常的查询和取反(NOT) 查询

语法示例:

```python
# 查询年龄30岁或者id为1的用户
Entry.objects.filter(Q(age=30)|Q(id=1))
# 查询出生年份不是1991年的用户
Entry.objects.filter(~Q(borthday__year ='1991'))
# 查询姓王且年龄为33岁的用户
Entry.objects.filter(Q(name__startswith='王')&Q(age=30))
```

## 13.原生sql查询

语法:

```python
Entry.objects.raw()
```

作用:

使用原生sql语句进行查询

语法示例:

```python
books = Book.objects.raw('select * from bookstore_book')
for book in books:
    print(book)
```

语法:

```python
connection.cursor()
```

作用:

在Django中跨过模型类直接操作数据库

示例:

```python
# 用SQL语句查询出所有的book"
from django.db import connection
with connection.cursor() as cur: 
cur.execute('select * from bookstore_book')
```



## 练习：

```python
# 查询出名字叫小明的年龄和地址
# 查询出所有的作者信息
# 查询出查找出版日期是2018年的书
# 查找2019年出版且价格大于300元的书名和价格
# 查找家住北京的作者
# 查找出2020年出版的图书并且以价格升序排列
```

