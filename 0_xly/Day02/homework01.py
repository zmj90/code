# 1 输入一个三位数（int），将数翻转,结果也是整型
# 输入：123
# 输出：321

# 输入：120
# 输出：21

# 输入：100
# 输出：1

# 规律：百位变个位，十位不变，个位变百位

# 方法1：
# number = int(input('请输入一个三位数：'))
#
# hundred = number // 100
# ten = number % 100 // 10
# one = number % 10
#
# result = hundred + ten * 10 + one * 100
#
# print('转换后的结果：', result)


# 方法2：
number = int(input('请输入一个三位数：'))

result = number // 100
result += number % 100 // 10 * 10
result += number % 10 * 100

print('转换后的结果：', result)