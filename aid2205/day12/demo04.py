"""
    重写算术运算符
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
        if type(other) == Vector2:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)  # 创建了新向量


pos01 = Vector2(1, 2)
pos02 = Vector2(3, 4)
pos03 = pos01 + pos02  # pos01.__add__(pos02)
pos04 = pos02 + pos01  # pos02.__add__(pos01)
pos05 = pos01 + 10  # pos01.__add__(10)
print(pos03)
