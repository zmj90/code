"""

"""


class CommodityModel:
    def __init__(self, name="", price=0, cid=0):
        self.name = name
        self.price = price
        self.cid = cid

    def __str__(self):
        return 'CommodityModel("%s",%s,%s)' % (self.name, self.price, self.cid)


tld = CommodityModel("屠龙刀", 10000, 101)

# 写入到文件中
with open("../data02.txt", "w", encoding="utf8") as file:
    file.write(tld.__str__() + "\n")

# 读取到程序中
with open("../data02.txt", encoding="utf8") as file:
    for item in file:
        print(eval(item))

# tld = CommodityModel("屠龙刀",10000,101)
# tld = eval('CommodityModel("屠龙刀",10000,101)')
