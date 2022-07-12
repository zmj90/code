"""
    画出下列代码内存图
"""
list01 = ["北京", "上海", "深圳"]
# 将列表地址赋值给list02
list02 = list01
list01.insert(0, "天津") # 元素向后移动
del list01[1] # 元素向前移动
print(list02)  # ?
