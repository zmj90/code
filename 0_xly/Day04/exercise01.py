# 定义函数：给定2个整数，当乘积大于1000时，返回乘积，否则返回总和。

# def compare(num01, num02):
#     '''
#         计算2个数的和或乘积
#     :param num01: 第1个数
#     :param num02: 第2个数
#     :return: 乘积或和
#     '''
#     res = num01 * num02
#     if res > 1000:
#         return res
#     else:
#         return num01 + num02
#
# # 接收compare函数的返回值赋值变量result
# result = compare(100, 2)
# print(result)


# def compare(num01, num02):
#     '''
#         计算2个数的和或乘积
#     :param num01: 第1个数
#     :param num02: 第2个数
#     :return: 乘积或和
#     '''
#     res = num01 * num02
#     if res > 1000:
#         return res
#     return num01 + num02
#
# result = compare(1000, 2)
# print(result)


def compare(num01, num02):
    '''
        计算2个数的和或乘积
    :param num01: 第1个数
    :param num02: 第2个数
    :return: 乘积或和
    '''
    res = num01 * num02
    if res <= 1000:
        res = num01 + num02
    return res

result = compare(1000, 2)
print(result)    # 11:46 上课
