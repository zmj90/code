"""
    需求：
        一家公司有如下几种岗位：
            --程序员:底薪 + 项目分红
            --测试员:底薪 + Bug数 * 5
        1. 创建员工管理器,储存所有员工
        2. 提供计算总薪资的方法
        要求:
            增加新岗位,员工管理器不受影响.
"""


class EmployeeController:
    def __init__(self):
        self.list_employee = []

    def add_employee(self, new):
        if isinstance(new, Employee):
            self.list_employee.append(new)

    def get_total_salary(self):
        total_salary = 0
        for item in self.list_employee:
            total_salary += item.calculate_salary()
        return total_salary


"""
class Employee:
    def calculate_salary(self):
        pass


# ----------------------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus
 
class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        self.base_salary = base_salary
        self.bug_count = bug_count

    def calculate_salary(self):
        return self.base_salary + self.bug_count * 5
"""


class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary


# ----------------------------------
class Programmer(Employee):
    def __init__(self, base_salary, bonus):
        super().__init__(base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        # return self.base_salary + self.bonus
        return super().calculate_salary() + self.bonus

class Tester(Employee):
    def __init__(self, base_salary, bug_count):
        super().__init__(base_salary)
        self.bug_count = bug_count

    def calculate_salary(self):
        return super().calculate_salary() + self.bug_count * 5
# ----------------------------------
controller = EmployeeController()
controller.add_employee(Programmer(10000,500000))
controller.add_employee(Tester(8000,120))
print(controller.get_total_salary())