"""
    小结 - 函数语法
        定义函数(做)
            def 函数名称(参数):
                函数体

        调用函数
            函数名称(数据)

    返回值语法
        调用者也可以不创建变量接收返回值
        Python语言函数默认返回None
        return还能退出函数
        函数没有return或者return后没有数据,都返回None
"""
def func01():
    print("func01执行了")
    return 100

def func02():
    print("func02执行了")

def func03():
    print("func03执行了")
    return 100 # return还能退出函数
    return 200
    print("func03又执行了")

def func04():
    print("func04执行了")
    return

# 调用者也可以不创建变量接收返回值
func01()
# Python语言函数默认返回None
data = func02()
print(data)

func03()

data02 = func04() # None
print(data02)