"""
    将面向过程代码改为面向对象代码
    练习:day09/homework/exercise01.py
"""

# 抽象的数据,操作数据的模板(格式)
class Restaurant:
    def __init__(self, city, name, remark=0, money=0):
        self.city = city
        self.name = name
        self.remark = remark
        self.money = money

# 自定义对象列表
list_restaurant = [
    Restaurant("北京","星期五餐厅",2847,180),
    Restaurant("北京","铁木真",3497,104),
    Restaurant("杭州","澳门豆捞",903,149),
    Restaurant("杭州","蒙太祖碳烤羊腿",37,230),
    Restaurant("上海","皇轶庭",421,110),
    Restaurant("上海","随缘蒸汽海鲜坊",682,128),
]

# -- 打印所有餐饮信息
# xx在xx地区,点评人数xx,人均消费xx元.
for item in list_restaurant:
    print("%s在%s地区,点评人数%s,人均消费%s元." % (
        item.name, item.city, item.remark, item.money))
    # print(f"{item.name}在{item.city}地区,点评人数{item.remark},人均消费{item.money}元.")

# -- 将人均150元以上的餐厅名称存入列表
list_name = []
for item in list_restaurant:
    if item.money > 150:
        list_name.append(item.name)
print(list_name)

# -- 查找点评人数最少的店铺（字典）
min_value = list_restaurant[0]
for i in range(1, len(list_restaurant)):
    if min_value.remark > list_restaurant[i].remark:
        min_value = list_restaurant[i]
print(min_value.__dict__)

# -- 根据人均对列表进行升序排列
for r in range(len(list_restaurant) - 1):
    for c in range(r + 1, len(list_restaurant)):
        if list_restaurant[r].money > list_restaurant[c].money:
            list_restaurant[r], list_restaurant[c] = list_restaurant[c], list_restaurant[r]
# 加断点
print(list_restaurant)
# 输出
# for item in list_restaurant:
#     print(item.__dict__)

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
# -- 打印所有餐饮信息
# xx在xx地区,点评人数xx,人均消费xx元.
for item in list_restaurant:
    print("%s在%s地区,点评人数%s,人均消费%s元." % (
        item["name"], item["city"], item["remark"], item["money"]))
    # print(f'{item["name"]}在{item["city"]}地区,点评人数{item["remark"]},人均消费{item["money"]}元.')

# -- 将人均150元以上的餐厅名称存入列表
list_name = []
for item in list_restaurant:
    if item["money"] > 150:
        list_name.append(item["name"])
print(list_name)

# -- 查找点评人数最少的店铺（字典）
min_value = list_restaurant[0]
for i in range(1, len(list_restaurant)):
    if min_value["remark"] > list_restaurant[i]["remark"]:
        min_value = list_restaurant[i]
print(min_value)

# -- 根据人均对列表进行升序排列
for r in range(len(list_restaurant) - 1):
    for c in range(r + 1, len(list_restaurant)):
        if list_restaurant[r]["money"] > list_restaurant[c]["money"]:
            list_restaurant[r], list_restaurant[c] = list_restaurant[c], list_restaurant[r]
print(list_restaurant)
"""