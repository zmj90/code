"""
    函数参数
        实际参数：如何与形参对应
            位置实参：按照顺序
                序列实参：使用容器包装信息,[拆]分后按顺序对应
            关键字实参：按照名称
                字典实参：使用容器包装信息,[拆]分后按顺序名称

        形式参数：约束实参传递方式
            默认参数：可选
            位置形参: 必填
                星号元组形参：使用容器包装信息,[合]并为一个元组
                       作用：位置实参可以数量无限
            命名关键字形参：强制要求使用关键字实参
                双星号字典形参：使用容器包装信息,[合]并为一个字典
                      作用：关键字实参可以数量无限
"""


#  2.位置形参：必填
def func01(p1, p2, p3):
    pass


# 位置实参:按顺序对应
func01(1, 2, 3)


# 1. 默认参数：可选
def func02(p1=0, p2="", p3=0.0):
    print(p1)
    print(p2)
    print(p3)


# 必须从右向左依次存在
def func03(p1, p2="", p3=0.0):
    print(p1)
    print(p2)
    print(p3)


# 3. 星号元组形参
def func04(*args):
    print(args)


func04()  # 没有实参,形参得到的是空元组()
func04(1, 2, 3)  # 有3个实参,形参得到的是1个元组(1, 2, 3)
list01 = ["a", "b"]
func04(*list01)  # 相当于 func04("a","b")  有2个实参,形参得到的是1个元组('a', 'b')


# func04(p1 = 1,p2 =2) 星号元组形参只负责合并位置实参(不管关键字实参)

# 4.命名关键字形参：强制要求使用关键字实参
# def 函数名称(*args,命名关键字形参1,命名关键字形参2)
# def 函数名称(*,命名关键字形参1,命名关键字形参2)
def func05(*args, p1, p2):
    print(args)


# func05(1,2,3,4)  语法错误
func05(1, 2, p1=3, p2=4)


def func06(p1, *, p2=0):
    print(p1)
    print(p2)


# p1 是常用的必填项,p2 是特殊场景可选项
func06(1, p2=2)  # 为了提高代码可读性

# def print(*args, sep=' ', end='\n', file=None)
# print("张三"," ") # 代码可读性差
print("张三", end=" ")
print("李四", end=" ")
# print(1,2,3,4,5,"-"," ")# 代码可读性差 1-2-3-4-5
print(1, 2, 3, 4, 5, sep="-", end=" ")  # 1-2-3-4-5


# 5. 双星号字典形参
def func07(**kwargs):
    print(kwargs)


func07(a=1, b=2, c=3)  # 传递三个关键字实参,形参接收的是一个字典{'a': 1, 'b': 2, 'c': 3}
func07()  # 没有,形参接收的是一个字典  {}
