# 随机产生一个数，循环猜测，直到猜对结束，提示大了、小了，猜对打印猜了多少次。


# 分析：
#  1 产生一个[1,100]之间的随机整数
#  2 循环输入（未知循环次数）：
#     while True:
#  3 输入一个整数，与随机数判断
#     整数 > 随机数，提示：大了
#     整数 < 随机数，提示：小了
#     整数 == 随机数，提示：猜对了
#  4 记次数：times=0
#     输入一次，记1次
#  5 打印共使用了多少次机会
#     猜对了打印次数


import random

# 产生一个[1, 100] 的随机整数
randNum = random.randint(1, 100)
print(randNum)

times = 0  # 记录次数

while True:
    UserNum = int(input('请输入猜测的数(0~100):'))
    times += 1  # 输入猜测一次记录1次

    if UserNum > randNum:
        print('大了')
    elif UserNum < randNum:
        print('小了')
    # elif UserNum == randNum:
    else:
        # print('猜对了')
        print('猜对了,共猜测了', times, '次')
        break

