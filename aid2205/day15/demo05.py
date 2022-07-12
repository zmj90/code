"""
    yield->生成器
"""
"""
class MyRange:
    def __init__(self,stop):
        self.stop = stop

    def __iter__(self):
        index = 0
        while index < self.stop:
            yield index
            index+=1
"""

# 生成器伪代码
"""
class generator:# 生成器 = 可迭代对象 + 迭代器
    def __iter__(self): # 可迭代对象
        return self
    def __next__(self): # 迭代器
        计算数据
        最后发送错误对象 
"""

def my_range(stop):
    index = 0
    while index < stop:
        yield index
        index+=1

# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
obj = my_range(50000) # 调用函数不执行,返回生成器对象
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item) # 0 1 2 3 4
    except StopIteration:
        break