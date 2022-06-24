"""
    核心数据类型
"""
# 1. Ｎｏｎｅ
a01 = "苏大强"
# 解除变量与数据的绑定关系
a01 = None
# 使用Ｎｏｎ占位
sex = None

# 2. 整形int
# 十进制
num01 = 20
# 二进制：０　　１　　１０　　１１　　 　１００　
print(0b10)# 2
# 八进制：0  1　．．7  10   11 ..
print(0o10)# 8
# 十六进制：0 -- 9   a(10) - f(15)
print(0x10)# 16

# 3.　浮点数float
print(1.5)
# 科学计数法:表示过小或过大的值很明确
# 1.23e-25
print(0.000000000000000000000000123)

# 4. 字符串str
print("1.5")
a = 10
print(a)# 打印变量　　10
print("a")# 打印字符串 a
"""
    核心数据类型
"""

# 1. 字符串str：存储多个文字
name01 = "金海"
# 判断变量所指向的数据类型
print(type(name01))

# 文字250
name01 = "250"
print(name01 + "1")  # 文字拼接 "2501"

# 2. 整型 int: 存储整数
# 数字250
number01 = 250
print(number01 + 1)  # 数字计算 251
# 十进制：逢十进一  0 1  2  3    4    5   ... 10
# 二进制：逢二进一  0 1 10 11  100   101
number02 = 0b10
# 八进制：逢八进一  0 1 2 3 ...           7  10
number03 = 0o10
# 十六进制：逢十六进一  0 1 2 3 ...         9   a(10) b c .. f(15)  10
number04 = 0x10
print(number02)
print(number03)
print(number04)

# 3. 浮点型float：小数
number05 = 1.23
print(type(number05))
# 科学计数法
number06 = 123e-2
print(number06)
print(0.00001)# 1e-05

# 4. 空类型None
# 占位
age = None

person_name = "金海"
# 解除与变量的绑定关系
person_name = None







