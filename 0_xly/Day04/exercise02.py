# 随机出题系统

# 符号：+ - *  /
# 数范围：1-100
# 题目：4 - 10 = -6
# 用户输入结果，比较是否正确，提示：正确错误
# 未知用户参与的次数，当输入的数据为空，结束
# 记录错误次数

import random


def calculate():
    error_times = 0   # 记录错误次数

    while True:
        # 1、构建式子：随机数1 随机符号 随机数2 =
        # 1、2个随机数
        num01 = random.randint(1, 100)
        num02 = random.randint(1, 100)

        # 2、随机1个符号
        operater = ['+', '-', '*', '/']
        sign = random.choice(operater)

        # 2、判断是：'+', '-', '*', '/'
        if sign == '+':
            res = num01 + num02
        elif sign == '-':
            res = num01 - num02
        elif sign == '*':
            res = num01 * num02
        else:  # sign == '/'
            res = int(num01 / num02)

        # 3、让用户输入结果
        user_res = input('{} {} {} = '.format(num01, sign, num02))

        # 1 判断输入是否为空，是空则结束
        if user_res == '':
            break   # 结束当前循环的

        # 2 判断输入值与电脑计算的结果比较，错误次数+1
        if int(user_res) != res:
            print('正确的为：{} {} {} = {}'.format(num01, sign, num02, res))
            error_times += 1

    # 4、打印错误的次数
    print('您本次共错误了{}次'.format(error_times))


# 函数调用：函数不调用，不会执行
calculate()
