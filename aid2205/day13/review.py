"""
    复习 - 面向对象语法
        1. 类和对象语法
            class 类名:
                def __init__(self,参数):
                    self.实例变量 = 参数
                    self.__私有实例变量 = 数据

                def 实例方法(self):
                    print(self.实例变量)
                    print(self.__私有实例变量)

            对象名 = 类名(数据)
            对象名.实例变量
            对象名.实例方法()
            # 无法访问私有实例变量

        2. 跨类调用
            # 方式1:直接创建对象
            # 语义：每次创建新对象
            class A:
                def func01(self):
                    b = B()
                    b.func02()

            class B:
                def func02(self):
                    pass
            a = A()
            a.func01()

            # 方式2:构造函数创建对象
            # 语义：每次使用旧对象
            class A:
                def __init__(self):
                    self.b = B()
                def func01(self):
                    self.b.func02()
            class B:
                def func02(self):
                    pass
            a = A()
            a.func01()
            a.func01()

            # 方式3:通过参数传递对象
            # 语义：灵活的使用对象
            class A:
                def func01(self,c):
                    c.func02()
            class B:
                def func02(self):
                    pass
            a = A()
            b = B()
            a.func01(  b  )
"""
class A(object):
    def __init__(self,num01,num02):
        self.num01 = num01
        self.num02 = num02

    def __eq__(self, other):
        return self.__dict__ ==other.__dict__

    def __gt__(self, other):
        return self.num01 > other.num01

list01 = [
    A(1,2),
    A(3,4),
    A(5,6),
]
print(A(5,6) in list01)
print(list01.count(A(1,2)))
list01.sort()
print(list01)

# tuple 是元组类
# (5,6) 是元组对象
list02 = [
    (1,2),
    (3,4),
    (5,6),
]
print((5,6) in list02) # True
# 列表.remove(元素)
# list02.remove((5,6))

# 查找元素数量
# 数量 = 列表.count(元素)
print(list02.count((1,2)))

# 查找元素索引
# 索引 = 列表.index(元素)
print(list02.index((3,4)))

list02.sort() # 升序排列
list02.sort(reverse=True) # 降序排列
print(list02)

