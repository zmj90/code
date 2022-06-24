# 字典 - dict

# 创建
# 空字典
# d = {}
# print(d, type(d))

# 非空字典
# print({'red':'红色', 'blue':'蓝色'})

# 键唯一
# print({'name':'python', 'name':'C'})
# # 键只能是：int/float/str
# print({1:'python', 1.2:'C'})
# # 无序
# print({1.2:'C', 1:'python'})
# print({1.2:'C', 1:'python'}==
#       {1:'python', 1.2:'C'})

# # 查看
# d = {'red': '红色',
#      'blue': '蓝色',
#      "1": '红色'}
# print('长度：', len(d))
# print('索引：', d['red'])
# print('索引：', d["1"])
# print('key存在：', 'red' not in d)
# print('key存在：', '红色' not in d)
#
# # 修改: key 存在
# d["1"] = 'Python'
# print(d)
#
# # 增加： key 不存在
# d["2"] = 'Java'
# print(d)
#
#
# # 删除
# del d['2']
# del d['1']
# print(d)

# 遍历
d = {'red': '红色',
     'blue': '蓝色',
     'orange': '橙色'}

# 方式1：
for k in d:
    print(k, d[k])

# 方式2：
for k, v in d.items():
    print(k, v)