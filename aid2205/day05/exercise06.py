"""
    画出下列代码内存图
"""
list01 = ["北京市", "上海市", "深圳"]
# 1
list02 = []
for item in list01:
    if len(item) == 3:
        list02.append(item)
print(list02) # ?

list02 = [item for item in list01 if len(item) == 3]


# 2
for i in range(len(list01)-1,-1,-1):
    list01[i] = list01[i][:2]
