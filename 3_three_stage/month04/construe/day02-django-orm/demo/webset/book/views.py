from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from book.models import Book,Author
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
import json

def get_data(requset):
#1.示意 基本查詢 all()
    # books = Book.objects.all()
    # for book in books:
    #     print("id:%s,書名:%s,出版時間:%s"%(book.id,book.title,book.publisher_date))
    # 全量的数据
    # id:1,書名:零基础学Python（全彩版）,出版時間:2020-01-09
    # id:2,書名:Python进行数据分析,出版時間:2019-05-08
    # id:3,書名:Python网络编程,出版時間:2020-05-10
    # id:4,書名:python爬虫,出版時間:2019-05-08
    # id:5,書名:python算法,出版時間:2018-04-18
    # id:6,書名:python测试,出版時間:2016-03-11
    # # 查看 query 打印輸出SQL語句,Queryset对象才有此属性.
    # print(books.query)
    # SELECT * FROM `book_book`
    #***************************************

#2.示意查詢返回部分列 values()
    # books = Book.objects.values("title","price")
    # for book in books:
    #     print(book)
        # print("書名:%s,出版日期:%s"%(book.get("title"),book.get("publisher_date")))
    # print(books.query)
    # SELECT `book_book`.`title`, `book_book`.`publisher_date` FROM `book_book`
    # SELECT `book_book`.`title`, `book_book`.`price` FROM `book_book`
    # {'title': '零基础学Python（全彩版）', 'price': Decimal('123.00')}
#3.示意 查詢返回部分列 返回值類型於2有所不同
    # books = Book.objects.values_list("title", "price")
    # for book in books:
    #     print(book)
    #     print("書名:%s,出版日期:%s"%(book[0],book[1]))
    # print(books.query)
    # SELECT `book_book`.`title`, `book_book`.`publisher_date` FROM `book_book`
    # ('零基础学Python（全彩版）', Decimal('123.00'))
    #***************************************
# 示意返回第一条数据:
    # book = Book.objects.first()
    # print(book)
    # 零基础学Python（全彩版）
# # 示意返回最后一条数据:
    # book = Book.objects.last()
    # print(book)
    # python测试
#4.示意 查詢只返回一條數據 get(),  只能使用等值做條件,查询出多条数据或者查询不到数据都会抛出异常.
    # book = Book.objects.get(id=10)
    # print("書名:%s,出版時間:%s"%(book.title,book.publisher_date))
    # 書名:零基础学Python（全彩版）,出版時間:2020-01-09
    # print(book.query)
    #***************************************

#5.示意 查詢根據條件查詢部分行數據 filter()
    #   1.查詢 id爲1 的 Book的信息
    # books = Book.objects.filter()
    # for book in books:
    #      print("id:%s,書名:%s,出版時間:%s"%(book.id,book.title,book.publisher_date))
    # id:1,書名:零基础学Python（全彩版）,出版時間:2020-01-09
    # print(books.query)
    # SELECT * FROM `book_book` WHERE `book_book`.`id` = 1
    #   2.查詢 publisher_date爲2015-10-12的book信息
    # books = Book.objects.filter(id=1,publisher_date='2020-01-09')
    # for book in books:
    #     print("書名:%s,出版時間:%s" % (book.title, book.publisher_date))
    # print(books.query)
    # SELECT * FROM `book_book` WHERE (`book_book`.`id` = 1 AND `book_book`.`publisher_date` = 2020-01-09)
    # 書名:零基础学Python（全彩版）,出版時間:2018-12-15
    #******************************************
    # books = Book.objects.filter(publisher_date__year__gt=2019)
    # for book in books:
    #     print("id:%s,書名:%s,出版時間:%s"%(book.id,book.title,book.publisher_date))
    # print(books.query)
    # id:1,書名:零基础学Python（全彩版）,出版時間:2020-01-09
    # SELECT * FROM `book_book` WHERE `book_book`.`id` < 2
    # SELECT * FROM `book_book` WHERE `book_book`.`publisher_date` > 2019-12-31

#6.示意 filter不等值查询 (屬性__謂詞)
    #   1.查詢2018年出版的書, 属性名(字段)__謂詞
    # books = Book.objects.filter(id__gt=4)
    # for book in books:
    #     print("書名:%s,出版時間:%s" % (book.title, book.publisher_date))
    # print(books.count)
    #   2.查詢 2017之後出版的書
    # books = Book.objects.filter(publisher_date__year__lt=2017)
    # for book in books:
    #     print("書名:%s,出版時間:%s" % (book.title, book.publisher_date))
#7. 示意 做不等值查詢 exclude(條件)
    #    1. 查詢 Author中年齡不大於20的人的信息
    # authors = Author.objects.all()
    # for author in authors:
    #     print(author.name,author.age,author.addr)
    # 小明 18 北京
    # 小红 30 上海
    # 小闹 24 广州
    # 小锟 1 北京

    # authors1 = Author.objects.filter(age__lte=20)
    # for author in authors:
    #     print("年齡不大於20的:%s"%author.name)
    # print(authors1.query)
    # 年齡不大於20的:小明
    # 年齡不大於20的:小锟
    # 年齡不大於20的:小明
    # 年齡不大於20的:小锟
    # SELECT * FROM `book_author` WHERE `book_author`.`age` <= 20

    # authors2 = Author.objects.exclude(age__gt=20)
    # for author in authors:
    #     print("年齡不大於20的:%s"%author.name)
    # print(authors2.query)
    # SELECT * FROM `book_author` WHERE NOT (`book_author`.`age` > 20)

#8. 示意排序查詢 order_by("列","-列")
    # authors = Author.objects.order_by("-age")
    # for author in authors:
    #     print("年齡升序排列:%s"%author.name,author.age)
    # print(authors.query)
    # SELECT * FROM `book_author` ORDER BY `book_author`.`age` ASC
    # SELECT * FROM `book_author` ORDER BY `book_author`.`age` DESC
#9. 示意聚合查詢 不分組類型 aggregate(鍵名=聚合函數("列名"))
    # 1.查詢Author表中所有人的平均年齡
    # authors = Author.objects.aggregate(avg=Avg("age"))
    # print(authors)
    # {'avg_age': 18.25}
    # {'avg': 18.25}
    # print("平均年齡:%s"%authors.get("avg"))
    # 平均年齡:18.25
#10. 示意聚合查詢 帶分組類型 annotate()
    # 1.查詢Book表中每個publisher_date所發型的書籍的數量
    # list = Book.objects.values("publisher_date").annotate(count=Count("title")).values("publisher_date","count").all()
    # print(list)
    # <QuerySet [
    # {'publisher_date': datetime.date(2020, 1, 9), 'count': 1}, 
    # {'publisher_date': datetime.date(2019, 5, 8), 'count': 2}, 
    # {'publisher_date': datetime.date(2020, 5, 10), 'count': 1}, 
    # {'publisher_date': datetime.date(2018, 4, 18), 'count': 1}, 
    # {'publisher_date': datetime.date(2016, 3, 11), 'count': 1}]
    # >
    # SELECT `book_book`.`publisher_date`,
    # COUNT(`book_book`.`title`) AS `count` 
    # FROM `book_book` 
    # GROUP BY `book_book`.`publisher_date` 
    # ORDER BY NULL

    # print(list.query)
# 示意Qureyset对象方法:
    # result = Book.objects.exists()
    # result = Book.objects.count()
    # print(result) #6
#11. 示意F查询
    # 查询id大于年龄的作者
    # authors = Author.objects.filter(id__gt=F('age'))
    # for author in authors:
    #     print(author.id,author.name)
    # Author.objects.filter(name='小锟').update(age=F('age')+20)
    # author = Author.objects.get(name='小锟')
    # print(author.id,author.name,author.age)
#12. 示意Q查询
    # 查询年龄30岁或id为1的用户
    authors = Author.objects.filter(Q(age=24) | Q(id=2))
    for author in authors:
        print(author.id,author.name,author.age)
    # 2 小红 30
    # 3 小闹 24
    # # 查询书的出版年份不是2018年的书籍
    books = Book.objects.filter(~Q(publisher_date__year ='2018'))
    for book in books:
        print(book.title,book.publisher_date)
    # 零基础学Python（全彩版） 2020-01-09
    # Python进行数据分析 2019-05-08
    # Python网络编程 2020-05-10
    # python爬虫 2019-05-08
    # python测试 2016-03-11
    # # 查询d开头且年龄为岁的用户
    return HttpResponse("<script>alert('查詢成功')</script>")