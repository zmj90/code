"""
    装饰器 - 原理推导
        为旧功能增加新功能,但是不用修改旧功能的定义与调用

        有外有内:外函数接收旧功能，包装包装新旧功能
        内使用外:希望新旧函数同时执行
        外返回内:希望后续逻辑可以不断使用新旧功能
"""
"""
def new_func():
    print("新功能")

def func01():
    print("旧功能")

# 旧功能不存在了
# func01 = new_func 

func01()
"""

"""
def new_func(func):
    print("新功能")
    func()

def func01():
    print("旧功能")

func01 = new_func ( func01 ) # 执行了新旧函数,返回了None
func01()
"""

def new_func(func): # 接收旧功能
    def wrapper(): # 包装新旧功能
        print("新功能")
        func()
    return wrapper

def func01():
    print("旧功能")

func01 = new_func ( func01 ) # 调用外函数,接收内函数

func01() # 执行内函数（新+旧）
func01() # 执行内函数（新+旧）
func01() # 执行内函数（新+旧）
func01() # 执行内函数（新+旧）