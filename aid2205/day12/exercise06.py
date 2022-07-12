"""
    练习：创建颜色类，数据包含r、g、b、a，实现颜色对象累加。
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.a == other.a


list_color = [
    Color(10, 10, 10, 10),
    Color(40, 40, 40, 40),
    Color(30, 30, 30, 30),
    Color(20, 20, 20, 20),
    Color(50, 50, 50, 50),
]

print(list_color.count(Color(20, 20, 20, 20)))
print(max(list_color))
list_color.sort()
print(list_color)  # 加断点调试
