"""
    使用自定义模块
"""
from common.iterable_tools import IterableHelper

list01 = [43, 85, 5, 67, 7]

def condition01(item):  # 4
    return item > 50

def condition02(item):
    return item < 10

def condition03(element):
    return element % 2 == 0

# 找第一个大于50的元素
print(IterableHelper.find_single(list01,condition01))
# 找所有小于10的元素
for item in IterableHelper.find_all(list01,condition02):
    print(item)
