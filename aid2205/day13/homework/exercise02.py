"""
    练习3：以面向对象思想,描述下列情景.
    # 行为相同的需求：
    张无忌教赵敏九阳神功
    赵敏教张无忌玉女心经
    张无忌工作挣了5000元
    赵敏工作挣了10000元

    # 行为不同的需求：
    张无忌教赵敏九阳神功
    赵敏工作挣了10000元
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def teach(self, other,skill):
        print(self.name, "教", other.name,skill)

    def work(self,salary):
        print(self.name,"挣了",salary,"元")

# 用对象区分数据不同
zwj = Person("张无忌")
zm = Person("赵敏")
# teach(self, other,skill)
# teach(zwj, zm,"九阳神功")
zwj.teach(zm,"九阳神功")
# teach(zm, zwj,"玉女心经")
zm.teach(zwj,"玉女心经")
zwj.work(5000)
zm.work(10000)
