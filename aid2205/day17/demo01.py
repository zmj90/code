"""
    内置高阶函数
"""

class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return str(self.__dict__)

list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

# 类似：IterableHelper.select
for item in map(lambda e: (e.name, e.money), list_employees):
    print(item)

# 类似：IterableHelper.find_all
for item in filter(lambda item: item.did == 9002, list_employees):
    print(item.__dict__)

# 类似：IterableHelper.get_max
# min
value = max(list_employees, key=lambda e: e.money)
print(value.__dict__)

# 升序排列
list_employees.sort(key=lambda e: e.money)
# 降序排列
list_employees.sort(key=lambda e: e.money, reverse=True)
print(list_employees)

# 不修改原列表,而是返回新列表
new_list = sorted(list_employees, key=lambda e: e.money)
new_list = sorted(list_employees, key=lambda e: e.money, reverse=True)
print(new_list)
