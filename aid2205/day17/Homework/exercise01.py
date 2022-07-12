"""
2. 使用IterableHelper完成下列功能
   在商品列表，获取所有名称与单价
   在商品列表中，获取所有单价小于10000的商品
   在商品列表中，获取编号是1005的商品
   对商品列表，根据单价进行升序排列
   获取元组中长度最大的列表  ([1,1],[2,2,2],[3,3,3])
"""

from common.iterable_tools import IterableHelper

class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
for item in IterableHelper.select(list_commodity_infos,lambda c: (c.name,c.price)):
    print(item)

for item in IterableHelper.find_all(list_commodity_infos,lambda cmd:cmd.price <10000):
    print(item.__dict__)

cmd = IterableHelper.find_single(list_commodity_infos,lambda item:item.cid == 1005)
print(cmd.__dict__)

IterableHelper.order_by(list_commodity_infos,lambda element:element.price)
print(list_commodity_infos)

tuple01 = ([1,1],[2,2,2],[3,3,3])
max_value = IterableHelper.get_max(tuple01,lambda item:len(item))
print(max_value) # [2, 2, 2]