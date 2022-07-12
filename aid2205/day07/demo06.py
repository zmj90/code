"""
    函数设计理念：
        崇尚小而精，拒绝大而全

    函数返回值
"""
# 需求：定义两个数字相加的函数
"""
def add():
    # 获取数据
    one = int(input("请输入第一个数字："))
    two = int(input("请输入第二个数字："))
    # 逻辑计算
    result = one + two
    # 显示结果
    print(f"结果是:{result}")

add()
"""


def add(one, two):
    # 逻辑计算
    data = one + two
    # print(result) # 不要显示结果
    return data  # 返回结果

number = add(6, 8)
print(number)
