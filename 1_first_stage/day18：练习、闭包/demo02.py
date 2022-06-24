"""
    外部嵌套作用域
"""

def fun01():
    # 是fun01函数的局部作用域
    # 也是fun02函数的外部嵌套作用域
    a = 1

    def fun02():
        b = 2
        # 可以访问外部嵌套作用域变量
        # print(a)
        # 不能修改外部嵌套作用域变量
        # a = 2# 创建了fun02的局部变量
        # print(a)# 2

        nonlocal a# 声明外部嵌套作用域
        a =2
        print(a)# 2

    fun02()
    print(a)# 1

fun01()



