"""
    练习:定义函数,数值累乘
"""
def multiplicative(*args):  # (5,15,1,581,61,6,49,14)
    number = 1
    for item in args:
        number *= item
    return number

# Python解释器自动构建元组,包装多个数据.
result = multiplicative(5, 15, 1, 581, 61, 6, 49, 14)
print(result)

