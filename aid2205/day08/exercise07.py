"""
输入1键：打印所有餐饮信息
输入2键：将人均150元以上的餐厅名称存入列表
输入3键：查找点评人数最少的店铺（字典）
输入4键：根据人均对列表进行升序排列
"""
list_restaurant = [
    {
        "city": "北京", "name": "星期五餐厅",
        "remark": 2847, "money": 180
    },
    {
        "city": "北京", "name": "铁木真",
        "remark": 3497, "money": 104
    },
    {
        "city": "杭州", "name": "澳门豆捞",
        "remark": 903, "money": 149
    },
    {
        "city": "杭州", "name": "蒙太祖碳烤羊腿",
        "remark": 37, "money": 230
    },
    {
        "city": "上海", "name": "皇轶庭",
        "remark": 421, "money": 110
    },
    {
        "city": "上海", "name": "随缘蒸汽海鲜坊",
        "remark": 682, "money": 128
    }
]


def print_restaurant_all():
    for item in list_restaurant:
        print("%s在%s地区,点评人数%s,人均消费%s元." % (
            item["name"], item["city"], item["remark"], item["money"]))


def find_name_by_money_gt_150():
    list_name = []
    for item in list_restaurant:
        if item["money"] > 150:
            list_name.append(item["name"])
    return list_name


def get_min_by_remark():
    min_value = list_restaurant[0]
    for i in range(1, len(list_restaurant)):
        if min_value["remark"] > list_restaurant[i]["remark"]:
            min_value = list_restaurant[i]
    return min_value


def ascending_by_money():
    for r in range(len(list_restaurant) - 1):
        for c in range(r + 1, len(list_restaurant)):
            if list_restaurant[r]["money"] > list_restaurant[c]["money"]:
                list_restaurant[r], list_restaurant[c] = list_restaurant[c], list_restaurant[r]


ascending_by_money()
print(list_restaurant)

value = get_min_by_remark()
print(value)

print_restaurant_all()
