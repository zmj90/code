"""
    内存图训练
"""
class MobilePhone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
# 1.
hua_wei = MobilePhone("华为",7000)
iphone =  hua_wei
iphone.brand = "苹果"
print(hua_wei.brand) # ?

# 2.
def func01(p1,p2):
    p1.brand = "huawei"
    p2 = MobilePhone("Iphone",8000)

hua_wei = MobilePhone("华为",7000)
iphone =  MobilePhone("苹果",8000)
func01(hua_wei,iphone)
print(hua_wei.brand)
print(iphone.brand)

# 3.
hua_wei = MobilePhone("华为",7000)
list_phone = [
    hua_wei,
    MobilePhone("苹果",8000)
]
total_price = 0
for item in list_phone:
    total_price += item.price
print(total_price) # ?


# 4.
list_phone = [
    MobilePhone("华为",7000),
    MobilePhone("苹果",8000)
]
def func01():
    list_brand = []
    for item in list_phone:
        list_brand.append(item.brand)
    return list_brand
list_data = func01()
print(list_data)