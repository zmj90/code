"""
    在地区列表中删除“浙江”
    在新增列表中删除第1个元素
    在现有列表中删除前2个元素
    在累计列表中删除全部元素
"""
list_region = ["台湾", "陕西", "浙江"]
list_new = [16, 182, 2]
list_now = [2339, 859, 505]
list_total = [16931, 1573, 2008]

if "浙江" in list_region:
    list_region.remove("浙江")

del list_new[0], list_now[:2], list_total[:]
