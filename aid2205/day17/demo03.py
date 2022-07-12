"""
    闭包-语法
        有外有内
        内使用外
        外返回内
"""


def func01():
    a = 10

    def func02():
        print(a)

    # return func02() # 调用内部函数,返回None
    return func02  # 返回内部函数

# 调用外函数,接收内函数
result = func01()
# 调用内函数
result()
