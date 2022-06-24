# 随机出题系统

# 符号：+ - *  /
# 数范围：1-100
# 题目：4 - 10 = -6
# 用户输入结果，比较是否正确，提示：正确错误
# 未知用户参与的次数，当输入的数据为空，结束
# 记录错误次数

import random


def create_exp():
    '''
        构建计算的式子
    :return: 计算的正确结果，表达的式子
    '''
    num01 = random.randint(1, 100)
    num02 = random.randint(1, 100)

    operater = ['+', '-', '*', '/']
    sign = random.choice(operater)

    if sign == '+':
        res = num01 + num02
    elif sign == '-':
        res = num01 - num02
    elif sign == '*':
        res = num01 * num02
    else:  # sign == '/'
        res = int(num01 / num02)

    str_exp = '{} {} {} = '.format(num01, sign, num02)
    # 电脑计算的正确结果、构建自定义的字符串
    return res, str_exp


def calcultor():
    '''
        用户参与计算
    :return: None
    '''
    error_times = 0  # 记录错误次数

    while True:
        # 构建式子
        true_res, exp = create_exp()

        user_res = input(exp)

        if user_res == '':
            break  # 结束当前循环的

        if int(user_res) != true_res:
            # 正确的为：{} {} {} =
            print('正确的为：{} {}'.format(exp, true_res))
            error_times += 1

    print('您本次共错误了{}次'.format(error_times))


# 函数调用：函数不调用，不会执行
calcultor()
