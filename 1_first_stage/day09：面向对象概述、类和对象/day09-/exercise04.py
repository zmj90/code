# 练习:定义函数,根据小时、分钟、秒,计算总秒数
# 调用：小时、分钟、秒  -->  总秒数
# 调用： 分钟、秒  -->  总秒数
# 调用： 分钟   -->  总秒数
# 调用： 小时、 秒    -->  总秒数
def calculate_second(hour=0, minte=0, second=0):
    return hour * 3600 + minte * 60 + second


print(calculate_second(1, 2, 3))  # 位置实参
print(calculate_second(minte=2, second=3))  # 关键字实参
print(calculate_second(minte=2))  # 关键字实参
# print(calculate_second(hour=1, second=3))  # 关键字实参
print(calculate_second(1, second=3))  # 位置实参 + 关键字实参
