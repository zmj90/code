"""
    生成器函数
        函数有多个结果使用yield返回
        函数有单个结果使用return返回
"""
# 需求：定义函数,找出所有大于100的数字
list01 = [45,346,45,756,8,67,887,9]

# 传统思想：创建列表存储所有结果
def find_numbers_gt_100():
    list_result = []
    for item in list01:
        if item > 100:
            list_result.append(item)
    return list_result

result = find_numbers_gt_100()
for item in result:
    print(item)

# 生成器思想：使用yield返回结果
def find_numbers_gt_100():
    for item in list01:
        if item > 100:
           yield item

result = find_numbers_gt_100()
for item in result:
    print(item)


