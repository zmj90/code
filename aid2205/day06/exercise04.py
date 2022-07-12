"""
    练习2：
        在终端中打印台湾的现有人数
        在终端中打印陕西的新增和现有人数
        浙江新增和现有人数各增加1
        广西现有和累计人数各减少2
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

print(dict_tan_wan["now"])
print(dict_shan_xi["new"])
print(dict_shan_xi["now"])
dict_zhe_jiang["new"] += 1
dict_zhe_jiang["now"] += 1
dict_guangxi["now"] -= 2
dict_guangxi["total"] -= 2
print(dict_zhe_jiang)
print(dict_guangxi)