"""
    变量交换
        a,b = b,a
    计算最值
        max_value = list01[0]
        for i in range(1,len(list01)):
            if max_value < list01[i]:
                max_value = list01[i]
        print(max_value)
    自定义排序算法
        升序排列：小->大
        降序排列：大->小
"""
#         0                len(列表)-1   len(list01)
list01 = [43, 5, 56, 6, 78, 8, 9]

"""
for i in range(1,len(list01)):
    if list01[0] < list01[i]:
        # 替换会丢失数据
        list01[0] = list01[i]
print(list01)
"""

"""
# 列表第一个元素是最大值
for i in range(1, len(list01)):
    if list01[0] < list01[i]:
        list01[0], list01[i] = list01[i], list01[0]
print(list01)

# 列表第二个元素是最大值
for i in range(2, len(list01)):
    if list01[1] < list01[i]:
        list01[1], list01[i] = list01[i], list01[1]
print(list01)

# 列表第三个元素是最大值
for i in range(3, len(list01)):
    if list01[2] < list01[i]:
        list01[2], list01[i] = list01[i], list01[2]
print(list01)

# ...
# 列表第倒数第二个元素是最大值 
"""

# 1.取数据
for r in range(len(list01)-1): #          0    1   2
    # 2.作比较
    for c in range(r + 1, len(list01)): # 123  23  3
        # 3.找更大
        if list01[r] < list01[c]:
            # 4.则交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
# 练习5： 对数字列表进行升序排列（小 --> 大）