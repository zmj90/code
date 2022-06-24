# 练习：输入一个三位数，计算百位、十位、个位上的和。
# 输入：234
# 输出：9

# number = int(input('请输入一个三位数：'))
#
# hundred = number // 100
# ten = number % 100 // 10
# one = number % 10
#
# result = hundred + ten + one
#
# print('和', result)


number = int(input('请输入一个三位数：'))

result = number // 100
result += number % 100 // 10
result += number % 10

print('和', result)
