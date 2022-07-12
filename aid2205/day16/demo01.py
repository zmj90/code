"""
    函数式编程
        理论支柱：将函数赋值给变量
"""


def func01():
    print("func01执行了")

# 1. 演示语法
func01()  # 直接调用

# a = func01() # 将函数的返回值给变量
a = func01  # 将函数赋值给变量

a() # 间接调用

# 2. 作用
def func02():
    print("func02执行了")

def func03(a):
    print("func03执行了")
    # func02() # 直接调用
    a() # 间接调用（限定此时只能调用无参数无返回值函数）
    # a(10) # （限定此时只能调用1个参数无返回值函数）

def func04(p):
    pass

func03(func02) #
func03(func01) #
# func03(func04) #
# ...