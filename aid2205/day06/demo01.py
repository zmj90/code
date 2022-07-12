list01 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
# 理解方式:数轴
for i in range(len(list01) - 1, -1, -1):  # 结束不包含-1,但是取到0
    print(list01[i])

# 理解方式:索引
# for item in list01[len(list01) - 1:-1:-1]: # 结束的-1指的是最后一个元素
#     print(item)

# for item in list01[::-1]: # 触发浅拷贝
#     print(item)
