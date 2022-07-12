"""
    在列表中查找最大值(不使用max,自定义算法实现)
    思路:
        假设第一个元素就是最大值
        依次与后面元素进行比较
        如果发现更大值,则替换
"""
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
max_value = list02[0]
for i in range(1, len(list02)):
    if max_value < list02[i]:
        max_value = list02[i]
print(max_value)
