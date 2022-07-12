"""
    练习2：定义函数,根据总两数,计算几斤零几两.:
    total_liang = int(input("请输入两:"))
    jin = total_liang // 16
    liang = total_liang % 16
    print(str(jin) + "斤零" + str(liang) + "两")
"""


def calculate_weight(total_liang):
    """
       根据总两数,计算几斤零几两.
    :param total_liang: int类型的总两数
    :return: 元组,(斤,两)
    """
    jin = total_liang // 16
    liang = total_liang % 16
    # return (jin, liang)
    return jin, liang  # 元组省略了小括号

# tuple_weight = calculate_weight(100)
# 建议使用拆包(左侧两个变量,右侧返回一个元组)
j, l = calculate_weight(100)
print(j)
print(l)
