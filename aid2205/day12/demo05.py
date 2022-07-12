"""
    重写增强运算符 += -= *= ...
"""


class Vector2:
    """
        二维坐标
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x的分量是{self.x},y分量是{self.y}"

    # + 自动执行
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)  # 创建了新向量

    # += 自动执行
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self  # 返回原始数据

pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
print(id(pos01))
pos01 += pos02  # pos01.__iadd(pos02)
print(id(pos01))

"""
list01 = [1]
list02 = [2]
print(id(list01))
list03 = list01 + list02  # 创建了新数据
print(id(list03))

list01 += list02  # 在原数据基础上改变
print(id(list01))
"""
