"""
    1. 打印第一条疫情信息,
       格式：xx地区新增xx人,现有xx人,累计xx人

    1. 打印所有疫情信息,
       格式：xx地区新增xx人,现有xx人,累计xx人

    2. 打印累计人数小于10000的所有疫情信息,
       格式：xx地区新增xx人,现有xx人,累计xx人



    3. 根据现有人数对疫情信息降序(大->小)排列
"""
list_epidemic = [
    {
        "region": "台湾", "new": 16,
        "now": 2339, "total": 16931,
    },
    {
        "region": "陕西", "new": 182,
        "now": 859, "total": 1573,
    },
    {
        "region": "浙江", "new": 2,
        "now": 505, "total": 2008,
    },
]

item = list_epidemic[0]
print(f"{item['region']}地区新增{item['new']}人,现有{item['now']}人,累计{item['total']}人")

for item in list_epidemic:
    print(f"{item['region']}地区新增{item['new']}人,现有{item['now']}人,累计{item['total']}人")

for item in list_epidemic:
    if item["total"] < 10000:
        print(f"{item['region']}地区新增{item['new']}人,现有{item['now']}人,累计{item['total']}人")

#  查找新增人数大于10的地区名称(将结果存入新列表)
list_region = []
for item in list_epidemic:
    if item["new"] > 10:
        list_region.append(item["region"])
print(list_region)

# 查找现有人数最大的地区信息(结果为字典)
max_value = list_epidemic[0]
for i in range(1, len(list_epidemic)):
    if max_value["now"] < list_epidemic[i]["now"]:
        max_value = list_epidemic[i]
print(max_value)

# 根据现有人数对疫情信息降序(大->小)排列
for r in range(len(list_epidemic) - 1):
    for c in range(r + 1, len(list_epidemic)):
        if list_epidemic[r]["now"] < list_epidemic[c]["now"]:
            list_epidemic[r], list_epidemic[c] = list_epidemic[c], list_epidemic[r]
print(list_epidemic)
