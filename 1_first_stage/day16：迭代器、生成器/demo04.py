"""
    yield --> 生成器
    练习:exercise07.py
"""
"""
class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        number = 0
        while number < self.stop_value:
            yield number
            number += 1

my01 = MyRange(10)

iterator = my01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
"""

"""
# 生成器原理
class MyGenerator:
    # 生成器 = 可迭代对象 + 迭代器
    def __init__(self,stop_value):
        self.begin = 0
        self.stop_value = stop_value
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.begin >= self.stop_value:
            raise StopIteration
            
        temp = self.begin
        self.begin+=1
        return temp
"""


def my_range(stop_value):
    number = 0
    while number < stop_value:
        yield number
        number += 1

my01 = my_range(10)
print(type(my01), dir(my01))# dir 获取对象所有成员

print(id(my01.__iter__()), id(my01))

for item in my01:
    print(item)


