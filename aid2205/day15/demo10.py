"""
    小结-列表与生成器
    列表
        优点：可以反复使用
            支持索引切片
            支持修改数据
        缺点：占用内存空间较大

    生成器
        优点：省内存(推算数据,存储当前数据,不存之前数据)
        缺点：生成器对象只能使用一次
             不支持索引切片
             不能修改数据
        适用性：优先
        解决：list(生成器)
"""

def my_range(stop):
    index = 0
    while index < stop:
        yield index
        index += 1

# 1. 演示：生成器对象只能使用一次
obj = my_range(5)
for number in obj:
    print(number)  # 0 1 2 3 4

for number in obj:
    print(number)  #


# obj = my_range(5)
# print(obj.__iter__()) # 0x000001F2F9125948
# print(obj.__iter__()) # 0x000001F2F9125948

# list01 = [1,2]
# print(list01.__iter__()) # 0x000001F2F9362A88
# print(list01.__iter__())# 0x000001F2F9362CC8
"""
class generator:# 生成器 = 可迭代对象 + 迭代器
    def __iter__(self): # 可迭代对象
        return self
    def __next__(self): # 迭代器
        计算数据
        最后发送错误对象 

obj = my_range(5)  
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item) # 0 1 2 3 4
    except StopIteration:
        break

iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item) # 0 1 2 3 4
    except StopIteration:
        break
"""

# 2. 演示：不支持索引切片
obj = my_range(5)
# print(obj[0])
# print(obj[-1])
# print(obj[-3:])
print(obj.__next__())