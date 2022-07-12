"""
    列表推导式
        根据可迭代对象,以简易的方式,构建新列表
"""
list01 = [34, 45, 65, 57, 78, 8]
# list02 = []
# for item in list01:
#     if item > 50:
#         list02.append(item)
list02 = [item for item in list01 if item > 50]



print(list02)  # [65, 57, 78]

# list03 = []
# for item in list01:
#     list02.append(item % 10)
list03 = [item % 10 for item in list01]
print(list03)
