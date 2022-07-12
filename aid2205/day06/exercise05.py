"""
    练习4：
    在终端中打印台湾所有键(一行一个)
    在终端中打印陕西所有值(一行一个)
    在终端中打印浙江所有键和值(一行一个)
    在广西字典中查找值是256对应的键名称
    删除广西新增留键人数保(通过键修改值)

    练习3：
    删除台湾现有信息
    删除陕西新增和现有信息
    删除浙江现有和累计信息
    删除广西新增人数保留键(通过键修改值)
"""
dict_tan_wan = {
    "region": "台湾",
    "new": 16,
    "now": 2339,
    "total": 16931
}
dict_shan_xi = {
    "region": "陕西",
    "new": 182,
    "now": 859,
    "total": 1573
}
dict_zhe_jiang = {
    "region": "浙江",
    "new": 2,
    "now": 505,
    "total": 2008
}
dict_guangxi = {
    "region": "广西",
    "new": 6,
    "now": 256,
    "total": 599
}

for key in dict_tan_wan:
    print(key)

for value in dict_shan_xi.values():
    print(value)

for key, value in dict_zhe_jiang.items():
    print(key)
    print(value)

for key, value in dict_guangxi.items():
    if value == 256:
        print(key)

dict_guangxi["new"] = 0
del dict_tan_wan["now"]
del dict_shan_xi["new"], dict_shan_xi["now"]
del dict_zhe_jiang["now"], dict_zhe_jiang["total"]

print(dict_tan_wan)
print(dict_shan_xi)
print(dict_zhe_jiang)
