"""
    函数内存分布
"""
# 1. 将函数代码存储在内存代码区(不执行函数体)
def func01(p):
    number = p + 5
    return number

num = 10
# 2. 调用函数时,在内存中开辟空间(栈帧)存储变量
data = func01(num)
# 3. 函数执行后,该空间立即释放
print(data)