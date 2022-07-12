"""
    比较运算符
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

    # 相同的依据
    def __eq__(self, other):
        # return self.x ==other.x and self.y == other.y
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.x > other.x


pos01 = Vector2(1, 1)
pos02 = Vector2(1, 1)
# 以下方法使用__eq__
# 默认比较地址
print(pos01 == pos02)  # pos01.__eq__(pos02)

list01 = [
    Vector2(1, 1),
    Vector2(2, 2),
    Vector2(4, 8000),
    Vector2(5, 5),
    Vector2(3, 3),
]
print(Vector2(1, 1) in list01)
list01.remove(Vector2(2, 2))
print(list01)

# 以下方法使用__gt__
print(max(list01))
list01.sort()
print(list01)
