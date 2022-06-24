# for循环语句

# 1、遍历字符串
# s = '我是中国人'
#
# for x in s:
#     print(x)



# range函数
# 需求1：打印10以内的所有整数 [0,9]
# start:0  stop:10 --> [0,9]
# for i in range(10):
#     print(i, end=' ')


# # 需求2：打印2-10之间的所有整数 [2,9]
# # start:2  stop:10 --> [2,9]
# for i in range(2, 10):
#     print(i, end=' ')


# 需求3：打印2-10之间的所有偶数
# start:2 stop:10 step:2 --> 2 4 6 8
# for i in range(2, 10, 2):
#     print(i, end=' ')


# 需求4：打印10-2之间的所有偶数
# start:10 stop:2 step:-2 --> 10 8 6 4
# for i in range(10, 2, -2):
#     print(i, end=' ')

#
# 步长：从小到大取值，start-stop取值是从大到小【方向相反】
# start与stop值一致
# for i in range(10, 10, 2):
#     print(i, end=' ')



# for + if语句
# 打印1-10之间的偶数
# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x, end=' ')



# while 与 for 在已知循环次数的差别

# x = 1
# while x < 5:
#     print(x, end=' ')
#     x += 2


# for y in range(5):
#     print(y, end=' ')
    # y += 2   不写