"""
    参数
        定义：函数调用者 给 函数定义者传递的信息
        本质就是由调用者确定的变量
"""


# 形参:假的抽象的
def attack(count):
    for number in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")


# 实参:真的具体的
attack(3)
c = 2
attack(c)
