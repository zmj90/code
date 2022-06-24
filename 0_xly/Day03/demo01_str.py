# 字符串 - str

# 重复
# s = 'python'
# print(s * 3)
# print('-' * 60)
# s *= 3
# print(s)


'https://sanguo.5000yan.com/1079.html'
'https://sanguo.5000yan.com/1080.html'
'https://sanguo.5000yan.com/1081.html'

# link = 'https://sanguo.5000yan.com/{}.html'
#
# for i in range(1070, 1081):
#     print(link.format(i))


# 打印：身高：xx,体重：xx, BMI:xxx，等级：xxx
height = 1.72
weight = 67
bmi = 22.8
level = '健康'

print('身高：', height,',体重：', weight,', BMI:', bmi,'，等级：', level)
print('身高：{},体重：{}, BMI:{}，等级：{}'.format(height, weight, bmi, level))

# s = '123'
# print(s[-1])
# s[-1] = "three"