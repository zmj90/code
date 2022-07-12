"""
    数据类型
"""
# 1. 字符串str:存储文本
name = "彭文韬"
print("25" + "1")  # 字符拼接

# 2. 整型int:存储整数
age = 25
print(25 + 1)  # 数学计算

# print("25" + 1) # 报错

# 3. 浮点型float:存储小数
score = 96.8

# input函数的结果一定是str
age = input("请输入年龄:") # "25"
print("明年你" + str(int(age) + 1) + "岁了")

# 4. 类型转换:  结果 = 目标类型(待转数据)
# str --> int
data01 = int("25")
# int --> str
data02 = str(25)

# str --> float
data03 = float("2.5")
# float --> str
data04 = str(2.5)

# int --> float
data05 = float(18)
print(data05) # 18.0
# float --> int
data06 = int(1.8) # 向下取整
print(data06) # 1   2

# 注意:str转换为其他类型时,必须"长的像"目标类型
# print(int("1.8")) # 报错
# print(int("彭文韬"))# 报错




