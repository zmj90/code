"""

"""
# 需求：累加1--100之间的整数
# 条件:能被3整除
# 思想:满足条件则累加
# value = 0
# for number in range(1,101):
#     if number % 3 == 0:
#         value += number
# print(value)

# 思想:不满足条件跳过,否则累加
value = 0
for number in range(1, 101):  # [100个瓜子]
    if number % 3 != 0:  # [如果遇到坏的]
        continue  # 跳过(继续下次循环) # [吐出来,继续嗑]
        # break # 跳出(结束循环)  # [吐出来,不再嗑]
    value += number  # [吃下去]
print(value)
