"""
    zip
        将多个可迭代对象中对应的元素,合并为元组
        生成器对象 = zip(可迭代对象1,可迭代对象2)
"""
list01 = [10, 20, 30]
list02 = ["a", "b", "c"]
list03 = [1.1, 1.2, 1.3]
for item in zip(list01, list02, list03):
    print(item)


map = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]
# 矩阵转置:行变列
"""
new_map = []
for item in zip(map[0],map[1],map[2],map[3]):
    new_map.append(list(item))
print(new_map)
"""

"""
new_map = []
for item in zip(*map):
    new_map.append(list(item))
print(new_map)
"""

new_map = [list(item) for item in zip(*map)]
print(new_map)
