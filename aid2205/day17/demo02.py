"""
    外部嵌套作用域
        在外函数中,内函数外创建的变量
        内函数可以读取,但是不能修改
        如果修改外部嵌套变量必须声明nonlocal
"""
g = 10


def func01():  # 外函数
    # 局部变量
    # 外部函数嵌套变量
    a = 10
    c = [10]
    def func02():  # 内函数
        # print(a) # 读取
        # 如果修改外部嵌套变量必须声明nonlocal
        nonlocal a
        a = 20  # 修改
        c[0] = 100
    func02()
    print(a,c)
# 不能直接调用func02
func01()
