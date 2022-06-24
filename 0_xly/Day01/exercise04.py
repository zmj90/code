# **练习2：输入计算机存储空间（MB）, 对应多少TB+多少GB+多少MB。**
# 输入：1050575
# 输出：1TB 1GB 975MB

# save = input('请输入容量空间（MB）:')   # MB
# save = int(save)

# save = int(input('请输入容量空间（MB）:'))  # MB

# print('TB:', save // (1024 * 1024))
# print('GB:', save % (1024 * 1024) // 1024)
# print('MB:', save % 1024)


save = int(input('请输入容量空间（MB）:'))  # MB

tb = save // (1024 * 1024)
gb = save % (1024 * 1024) // 1024
mb = save % 1024
print('TB:', tb, 'GB:', gb, 'MB:', mb)

# 验算结果
print(tb * 1024 ** 2 + gb * 1024 + mb)

# print(1 * 1024 ** 2 + 1 * 1024 + 975)
# print(1 * 1024 ** 2 + 6 * 1024 + 855)
