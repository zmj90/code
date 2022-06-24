# 练习1：输入一个三位数，分别打印出百位、十位、个位上的数字。
# 输入：234
# 输出：百位是2，十位是3，个位是：4

number = int(input('请输入一个三位数：'))

hundred = number // 100
ten = number % 100 // 10
one = number % 10

print('百位是', hundred,
      '，十位是', ten,
      '，个位是：', one)

# number = 120
#
# print('百位：', number // 100)
# print('十位：', number % 100 // 10)
# print('十位：', number // 10 % 10)
# print('个位：', number % 10)
