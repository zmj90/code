"""
    练习4：
        在员工列表中查找所有部门是9002的员工
        在员工列表中查找编号是1003的员工
        累加员工列表中所有员工薪资
        print(IterableHelper.find_single(list01, lambda item: item > 50))

"""
from common.iterable_tools import IterableHelper


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

# 在员工列表中查找所有部门是9002的员工
for item in IterableHelper.find_all(list_employees, lambda e: e.did == 9002):
    print(item)
# 在员工列表中查找编号是1003的员工
print(IterableHelper.find_single(list_employees, lambda item: item.eid == 1003))
# 累加员工列表中所有员工薪资
print(IterableHelper.sum(list_employees, lambda e: e.money))
