"""
    函数式编程思想
        适用性：多个函数主体结构相同,但是核心算法不同
        步骤:
            "封装"[分]：将变化的需求分为多个函数
            "继承"[隔]：将变化函数抽象为参数,
                       统一变化函数的定义(参数、返回值)
            "多态"[做]：因为：
                        编码时通用函数调用的是参数
                        运行时执行传入的变化函数
                       所以：
                        增加的变化函数必须与参数的使用相同
"""
list01 = [43, 85, 5, 67, 7]


# 查找第一个大于50的数字
def get_number_gt_50():
    for item in list01:
        if item > 50:
            return item


# 查找第一个小于10的数字
def get_number_lt_10():
    for item in list01:
        if item < 10:
            return item


# 参数：列表中的元素；返回值：传递给get_number的if
def condition01(item):  # 4
    return item > 50


def condition02(item):
    return item < 10

# 通用函数
def get_number(condition):  # 2
    for item in list01:
        # if item < 10:
        # if condition02(item):
        # if condition01(item):
        # 使用参数
        if condition(item):  # 3 (限定此时传入的函数必须有1个参数1个返回值)
            return item

# 变化函数
def condition03(element):
    return element % 2 == 0

print(get_number(condition01))  # 1
print(get_number(condition03))  # 1
