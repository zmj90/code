"""
    练习7：get_max
        定义函数，在员工列表中查找薪资最高的员工
        定义函数，在员工列表中查找员工编号最大的员工
        步骤：
            -- 根据需求，写出函数。
            -- 因为主体逻辑相同,核心算法不同.
               所以使用函数式编程思想(隔、做)
               创建通用函数,添加到IterableHelper中
            -- 在当前模块中调用
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

"""
def get_max01():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.money < list_employees[i].money:
            max_value = list_employees[i]
    return max_value


def get_max02():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.eid < list_employees[i].eid:
            max_value = list_employees[i]
    return max_value


print(get_max01())


def get_max(condition):
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if max_value.eid < list_employees[i].eid:
        if condition(max_value) < condition(list_employees[i]):
            max_value = list_employees[i]
    return max_value

print(get_max(lambda item: item.eid))
"""

print(IterableHelper.get_max(list_employees, lambda e: e.money))