"""
    业务逻辑层
"""
from dal import HouseDao


class HouseManagerController:
    """
        房源信息管理系统控制器：负责处理业务逻辑
    """

    def __init__(self):
        """
            创建房源信息管理系统控制器
        """
        self.__dao = HouseDao()
        self.list_houses = self.__dao.load()

    def get_house_by_max_total_price(self):
        # 写法1：简单但不灵活
        # 重写模型的__gt__方法
        # return max(self.list_houses)

        # 写法2： 内置高阶函数
        return max(self.list_houses,key = lambda house:house.total_price)
