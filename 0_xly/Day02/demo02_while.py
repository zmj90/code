# while 循环语句

# # 需求1：打印1-10之间的整数 [1,9]
# # 初始条件
# x = 1
# while x < 10:  # 循环9次
#     print(x, end=' ')
#     x += 1  # 变化条件
# else:  # x = 10
#     print('执行else语句')


# # 需求2：打印1-10之间的奇数
# # 初始条件
# x = 1
# while x < 10:
#     print(x, end=' ')
#     x += 2  # 变化条件


# 需求3：打印1-10之间的偶数
# while + if
# 初始条件
x = 1
while x < 10:
    if x % 2 == 0:
        print(x, end=' ')

    x += 1  # 变化条件