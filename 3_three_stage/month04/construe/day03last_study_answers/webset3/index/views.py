from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile,WeiboUser,SKU,OrderInfo,OrderGoods,Student,Course
# Create your views here.
def index(request):
    # user1 = UserProfile.objects.create(username='小泽',password='123456',email='lvze@tedu.cn')
    # wuser1 = WeiboUser.objects.create(user=user1,uid='清风徐来',access_token='')
    # user2 = UserProfile.objects.create(username='小闹',password='123456',email='bjjtguojy@tedu.cn')
    # wuser2 = WeiboUser.objects.create(user=user2,uid='晨晨',access_token='')
    # user3 = UserProfile.objects.create(username='小文',password='123456',email='shibw@tedu.cn')
    # wuser3 = WeiboUser.objects.create(user=user3,uid='文武双全',access_token='')    
    # sku1 = SKU.objects.create(name='红袖添香',price=200,stock=1000,sales=1000,comments=800)
    # sku2 = SKU.objects.create(name='绿野仙踪',price=150,stock=1000,sales=1000,comments=800)
    # sku3 = SKU.objects.create(name='黄色闪光',price=100,stock=1000,sales=1000,comments=800)
    # sku4 = SKU.objects.create(name='紫色激情',price=80,stock=1000,sales=1000,comments=800)
    # order1 = OrderInfo.objects.create(order_id='2019111118050001',user=user1,total_count=3,total_amount=560)
    # order2 = OrderInfo.objects.create(order_id='2012111118050002',user=user2,total_count=1,total_amount=200)
    # order3 = OrderInfo.objects.create(order_id='2015111118050003',user=user3,total_count=3,total_amount=350)
    # order4 = OrderInfo.objects.create(order_id='2020051312000001',user=user1,total_count=1,total_amount=200)
    # order5 = OrderInfo.objects.create(order_id='2020052312000003',user=user3,total_count=1,total_amount=200)
    # ordergood1 = OrderGoods.objects.create(order=order1,sku=sku1,count=1,price=250)
    # ordergood2 = OrderGoods.objects.create(order=order1,sku=sku2,count=1,price=150)
    # ordergood3 = OrderGoods.objects.create(order=order1,sku=sku1,count=2,price=160)
    # ordergood4 = OrderGoods.objects.create(order=order2,sku=sku1,count=1,price=200)
    # ordergood5 = OrderGoods.objects.create(order=order3,sku=sku3,count=2,price=100)
    # ordergood6 = OrderGoods.objects.create(order=order3,sku=sku2,count=1,price=150)
    # ordergood7 = OrderGoods.objects.create(order=order4,sku=sku1,count=1,price=200)
    # ordergood8 = OrderGoods.objects.create(order=order5,sku=sku1,count=1,price=200)
    # student1 = Student.objects.create(name='张三',class_room='三年二班')
    # student2 = Student.objects.create(name='李四',class_room='三年三班')
    # student3 = Student.objects.create(name='王二',class_room='三年四班')
    # course1 = student1.course_set.create(name='python基础') 
    # student2.course_set.add(course1)
    # course2 = student3.course_set.create(name='python网络编程')
    # student2.course_set.add(course2)
    # course3 = student1.course_set.create(name='python后端开发')
    # student3.course_set.add(course3)
    


    # 通过userprofile查找weibouser的uid
    # user = UserProfile.objects.get(username='小泽')
    # print(user.weibouser.uid)
    # 通过weibouser查询userprofile的email
    # wuser = WeiboUser.objects.get(uid='清风徐来')
    # print(wuser.user.email)

    # 清风徐来
    # lvze@tedu.cn    

    # # 通过order查询出所有的ordergoods的价格
    # 拿到订单
    # order = OrderInfo.objects.get(order_id='2019111118050001')
    # 通过订单下的所有商品
    # goods = order.ordergoods_set.all()
    # # 获取商品价格
    # for good in goods:
    #     print('商品:%s的价格:%s'%(good.sku.name,good.price))
    
    # 商品:红袖添香的价格:250.00
    # 商品:绿野仙踪的价格:150.00
    # 商品:红袖添香的价格:160.00


    # # 通过student查询出选修的所有课程
    # student = Student.objects.get(name='张三')
    # courses = student.course_set.all()
    # for course in courses:
    #     print('学生:%s选修了%s'%(student.name,course.name))

    # 学生:张三选修了python基础
    # 学生:张三选修了python后端开发


    # # 查询出订单2019111118050001购买者的邮箱
    order = OrderInfo.objects.get(order_id='2019111118050001')
    print(order.user.email)

    # # 看文武双全买了那些商品，打印商品名
    # wuser = WeiboUser.objects.get(uid='文武双全')
    # user = wuser.user
    # orders = user.orderinfo_set.all()
    # for order in orders:
    #     goods = order.ordergoods_set.all()
    #     for good in goods:
    #         print('订单:%s中有商品%s'%(order.order_id,good.sku.name))
    
#     订单:2015111118050003中有商品黄色闪光
#     订单:2015111118050003中有商品绿野仙踪
#     订单:2020052312000003中有商品红袖添香

    # # 查询出订单2015111118050003中的商品库存还剩多少
    # order = OrderInfo.objects.get(order_id='2015111118050003')
    # goods = order.ordergoods_set.all()
    # for good in goods:
    #     print('商品%s还剩%d件'%(good.sku.name,good.sku.stock))

    # # 查询出订单2019111118050001中价格最便宜的商品价格
    from django.db.models import Avg,Count,Max,Min,Sum,F,Q
    order = OrderInfo.objects.get(order_id='2019111118050001')
    goods = order.ordergoods_set.aggregate(min_price=Min("price"))
    print('订单:%s中最便宜的商品为:%s'%(order.order_id,goods.get('min_price')))
    # 订单:2019111118050001中最便宜的商品为:150.00
    # # 查询出python基础被那些学生选修
    course = Course.objects.get(name='python基础')
    students = course.students.all()
    print('选修python基础的有:')
    for student in students:
        print(student.name)
    # 选修python基础的有:
    # 张三
    # 李四
    return HttpResponse('ok')