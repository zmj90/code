"""
    创建图形管理器
    -- 记录多种图形（圆形、矩形....）
    -- 提供计算总面积的方法.
    要求：增加新图形，不影响图形管理器.
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.

    封装[分]：分而治之，变则疏之
            例如：创建图形管理器、圆形、矩形..
    继承[隔]：统一行为，隔离变化
            例如：创建图形类,统一圆形、矩形的计算面积方法
                图形类隔离了图形管理器和圆形、矩形
    多态[做]：编码时调用父，运行时执行子
            例如：图形管理器调用图形方法
                 圆形、矩形重写图形方法
"""

"""
class GraphicsController:
    def __init__(self):
        self.list_graphics = []

    def get_total_area(self):
        total_area = 0
        for item in self.list_graphics:
            # 编码时,调用的是父类
            # 运行时,执行的是子类
            total_area += item.calculate_area()
        return total_area


class Graphics:
    def calculate_area(self):
        pass


# --------------------------------------------
class Circle(Graphics):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w


# --------------------------------------------
controller = GraphicsController()
# 向图形管理器添加的是具体图形(子类对象)
controller.list_graphics.append(Circle(5))
controller.list_graphics.append(Rectangle(2, 6))
print(controller.get_total_area())
"""

class GraphicsController:
    def __init__(self):
        self.__list_graphics = []

    def add_graphics(self,new):
        # 添加的必须是一种图形(有继承关系)
        if isinstance(new,Graphics):
            self.__list_graphics.append(new)

    def get_total_area(self):
        total_area = 0
        for item in self.__list_graphics:
            total_area += item.calculate_area()
        return total_area


class Graphics:
    def calculate_area(self):
        pass


# --------------------------------------------
class Circle(Graphics):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return 3.14 * self.r ** 2


class Rectangle(Graphics):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_area(self):
        return self.l * self.w


# --------------------------------------------
controller = GraphicsController()
controller.add_graphics(Circle(5))
controller.add_graphics(Rectangle(2, 6))
controller.add_graphics("三角形")
print(controller.get_total_area())