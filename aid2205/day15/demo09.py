"""
    列表推导式
    生成器表达式 
"""
list01 = [34, 45, 65, 57, 78, 8]
# list02 = [item for item in list01 if item > 50]
generator01 = (item for item in list01 if item > 50)
for item in generator01:
    print(item)

# list03 = [item % 10 for item in list01]
generator02 = (item % 10 for item in list01)
for item in generator02:
    print(item)
# 练习1：使用生成器表达式在列表中获取所有字符串.
# list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]
# 练习2：在列表中获取所有整数,并计算它的平方.

