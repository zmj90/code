"""
    lambda 表达式
        匿名函数
            lambda 参数:函数体

        lambda可以完成的任务,def都可以
        lambda函数体只能有一句话，且不支持赋值
"""
# 1. 有参数有返回值
# def func01(p1,p2):
#     return  p1 >p2
#
# print(func01(1, 2))

func01 = lambda p1, p2: p1 > p2
print(func01(1, 2))

# 2. 有参数无返回值
# def func02(p1):
#     print("参数是：",p1)
#
# func02(1)

func02 = lambda p1: print("参数是：", p1)
func02(1)

# 3. 无参数有返回值
# def func03():
#     return 10
#
#
# print(func03())

func03 = lambda: 10
print(func03())


# 4. 无参数无返回值
def func04():
    print("hello world")


func04()

func04 = lambda: print("hello world")


# 注意1:lambda函数体只能有1句话
def func05():
    for item in range(10):
        print(item)


func05()


# lambda :for item in range(10):
#     print(item)

# 注意2:lambda函数不支持赋值语句
def func06(p):
    p[0] = 100

list01 = [10]
func06(list01)
print(list01)  # [100]

# lambda p: p[0] = 100


