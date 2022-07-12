"""
    内置生成器函数
       生成器对象 = enumerate(可迭代对象)
       for 索引,元素 in 生成器对象:
"""
list01 = [43,54,6,7,8,9]
# 从头到尾读取
for item in list01:
    print(item)
# 从头到尾读改
for i in range(len(list01)):
    if list01[i] > 10:
        list01[i] = 10

# 遍历可迭代对象时,可以同时获得索引与元素
for i,item in enumerate(list01):
    if item > 10:
        list01[i] = 10

# 练习1：将列表中所有奇数设置为None
# 练习2：将列表中所有偶数自增1


