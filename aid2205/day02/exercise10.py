"""
    练习：在终端中输入一个四位整数，计算每位相加和。
    例如：录入1234，打印1+2+3+4结果
    效果：
    请输入四位整数：1234
    结果是：10
"""
# 写法1:相加
number = int(input("请输入数字："))  # 1234
unit01 = number % 10  # 个位
# 1234  // 10 -> 123 % 10 -> 3
unit02 = number // 10 % 10  # 十位
# 1234  // 100 -> 12 % 10 -> 2
unit03 = number // 100 % 10  # 百位
unit04 = number // 1000  # 千位
sum_value = unit01 + unit02 + unit03 + unit04
print("累加和是:"+str(sum_value))

# 写法2:累加
number = int(input("请输入数字："))  # 1234
sum_value = number % 10  # 个位
sum_value += number // 10 % 10  # 十位
sum_value += number // 100 % 10  # 百位
sum_value += number // 1000  # 千位
print("累加和是:"+str(sum_value))