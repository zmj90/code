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

    # 获取计算的正确结果
    expression = str(num01) + sign + str(num02)
    true_res = eval(expression)

    str_exp = '{} {} {} = '.format(num01, sign, num02)

    # 电脑计算的正确结果、构建自定义的字符串
    return true_res, str_exp

def save_data(lists):
    '''
        将列表中的数据写入文件中
    :param lists: 存储式子的列表
    :return: None
    '''
    file_obj = open('错题本.txt', 'a')

    # error_exp = '\n'.join(lists)
    error_exp = ''
    for exp in lists:
        error_exp += exp + '\n'

    file_obj.write(error_exp)
    file_obj.close()


def calcultor():
    '''
        用户参与计算
    :return: None
    '''
    error_times = 0  # 记录错误次数

    list_error = []  # 存储错误题目
    while True:
        # 构建式子
        true_res, exp = create_exp()

        user_res = input(exp)

        if user_res == '':
            break  # 结束当前循环的

        # eval(str)   将str作为表达式执行
        if eval(user_res) != true_res:
            # 正确的为：'{} {} {} ='
            print('正确的为：{} {}'.format(exp, true_res))
            error_times += 1

            list_error.append('{}{}'.format(exp, true_res))

            print('错误列表:', list_error)
    print('您本次共错误了{}次'.format(error_times))

    # 将错误的题目存储至文件中
    save_data(list_error)

# 函数调用：函数不调用，不会执行
calcultor()
