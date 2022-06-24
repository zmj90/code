# 练习2：彩票生成器
# 产生一注双色球并打印。
# 红色：取值 [1, 33]
# 蓝色：取值 [1, 16]
# 规则：
# ​	1、一共是7个球（6红1蓝）
# ​	2、6个红色的数字不能相同
import random

# 1 创建空列表：存储6红1蓝
lists = []

# 2 存储红球：未知循环次数
while True:
    #   1 随机[1,33]之间的整数，存储到列表
    num = random.randint(1, 33)

    #   2 判断随机数是否在列表中存在
    #     不存在：存列表
    if num not in lists:
        lists.append(num)

    print(lists)

    #   3 结束：列表长度为6，break
    if len(lists) == 6:
        lists.sort()
        break

# 3 随机[1,16]之间的整数添加到列表中
blue = random.randint(1, 16)
lists.append(blue)
print('一注彩票：', lists)