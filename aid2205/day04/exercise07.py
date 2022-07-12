"""
    创建地区列表、新增列表、现有列表，
    累计列表分别存储3行(台湾、陕西、浙江)信息

    向以上四个列表追加数据第4行(广西)信息
    在第1个位置插入第5行(香港)信息
"""
list_region = ["台湾", "陕西", "浙江"]
list_new = [16, 182, 2]
list_now = [2339, 859, 505]
list_total = [16931, 1573, 2008]

list_region.append("广西")
list_new.append(6)
list_now.append(256)
list_total.append(599)

list_region.insert(0, "香港")
list_new.insert(0, 9)
list_now.insert(0, 196)
list_total.insert(0, 12598)

print(list_region)
print(list_new)
print(list_now)
print(list_total)
