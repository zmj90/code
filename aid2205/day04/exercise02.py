"""
    练习：累加10 -- 60之间，个位不是3/5/8的整数和。
     -- 思路1：不是3/5/8则累加
     -- 思路2：是3/5/8则跳过,否则累加
"""

"""
value = 0
for number in range(10,61):
    if number % 10 != 3 and number % 10 != 5 and number % 10 != 8:
        value += number
print(value)
"""
# 思路1：不是3/5/8则累加
value = 0
for number in range(10, 61):
    unit = number % 10
    if unit != 3 and unit != 5 and unit != 8:
        value += number
print(value)

# 0 1 2 3 4 5 6 7 8 9
# 思路2：是3/5/8则跳过,否则累加
value = 0
for number in range(10, 61):
    unit = number % 10
    if unit == 3 or unit == 5 or unit == 8:
        continue
    value += number
print(value)
