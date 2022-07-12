"""
    装饰器 - 标准
        @装饰器名称
        内函数返回值是旧功能返回值
        装饰器通过*args合并、拆分参数
"""


def new_func(func):
    def wrapper(*args,**kwargs): # 2  合并
        print("新功能")
        result = func(*args,**kwargs) # 3 拆分
        return result
    return wrapper

# func01 = new_func ( func01 )
@new_func # 调用外函数,将内函数赋值给旧功能
def func01(p1,p2): # 4
    print("旧功能")
    return 100

print(func01(10,20)) # 1 调用内函数
