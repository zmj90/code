"""
    运算符
        算术运算符:+ - *
                  幂运算**
                  小数商 /
                  整数商 //
                  余数 %

        增强运算符:+= -= *=
                  幂运算**=
                  小数商 /=
                  整数商 //=
                  余数 %=
        (在算术运算符基础上增加对自身的赋值)
"""
number01 = 5
number02 = 2
# 算术运算符
print(number01 ** number02)  # 25
print(number01 % number02)  # 1
print(number01 / number02)  # 2.5
print(number01 // number02)  # 2
# 增强运算符
# number01 + 5 # 不改变旧数据
# print(number01) # 5

# number01 = number01 + 5
number01 += 5 # 累加
print(number01)  # 10

# print(number01 + 5)
# print(number01 += 5) # 报错

