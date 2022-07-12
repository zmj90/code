"""

"""
# -----------------全局变量----------------------

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


# -----------------定义函数----------------------

# 定义函数,打印所有疫情信息
def print_epidemic_all():
    for item in list_epidemic:
        print(f"{item['region']}地区新增{item['new']}人,现有{item['now']}人,累计{item['total']}人")


#  查找新增人数大于10的地区名称(将结果存入新列表)
def get_region_new_gt_10():
    list_region = []
    for item in list_epidemic:
        if item["new"] > 10:
            list_region.append(item["region"])
    return list_region


# 查找现有人数最大的地区信息(结果为字典)
def get_max_by_now():
    max_value = list_epidemic[0]
    for i in range(1, len(list_epidemic)):
        if max_value["now"] < list_epidemic[i]["now"]:
            max_value = list_epidemic[i]
    return max_value


# 根据现有人数对疫情信息降序(大->小)排列
def descending_order_by_now():
    for r in range(len(list_epidemic) - 1):
        for c in range(r + 1, len(list_epidemic)):
            if list_epidemic[r]["now"] < list_epidemic[c]["now"]:
                # 因为修改列表元素,没有修改全局变量,所以不用global
                list_epidemic[r], list_epidemic[c] = list_epidemic[c], list_epidemic[r]


# -------------------调用函数--------------------
print_epidemic_all()
result = get_region_new_gt_10()
print(result)
value = get_max_by_now()
print(value)
descending_order_by_now()
print(list_epidemic)
