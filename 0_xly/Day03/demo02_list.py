# 列表 - list

# 创建
# 空列表
# list01 = []
# print(list01, type(list01))

# 非空列表
# print([3, 4.45, 'python', [3, 5]])

# list(可迭代对象)
# print(list(range(1,10)))
# print(list('python'))


# 增加
# list02 = ['python']
# list02.append('java')  # 追加
# list02.append('SQL')  # 追加
# list02.append('JavaScript')  # 追加
# print(list02)

# 查看
# print(len(list02))  # 长度
# print(list02[-2])  # 索引
# print(list02[:3])  # 切片
# print(list02[:-1])  # 切片
# print('Java' in list02)
# print('java' in list02)
# print('java' not in list02)

# 修改
# list02[-1] = 'JS'
# print(list02)
#
# # 删除
# del list02[1]
# print(list02)
#
# # 排序
# list03 = [1, 6, 3, 9, 2]
# # list03.sort()   # 升序
# list03.sort(reverse=True)   # 降序
# print(list03)
#
# # 遍历
# for x in list03:
#     if x % 2 == 1:
#         print(x, end=' ')
#
#
# for x in range(len(list03)):
#     print(x, list03[x])


# 与字符串的互操作

# list --> str
list04 = ['荣耀', 'P40', 'Plus']
result = '_'.join(list04)
print(result)

date = '2022/02/22'
res = date.split('/', 1)
print(res)

house_info = '112m | 南北 | 毛坯'
print(house_info.split(' | '))

house_info = '112m  南北 毛坯'
print(house_info.split())