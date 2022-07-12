"""
    用户显示层
"""
from bll import HouseManagerController


class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1键显示所有房源信息")
        print("2键显示总价最高的房源信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__show_houses()
        elif item == "2":
            self.__show_house_by_max_total_price()

    def __show_houses(self):
        for house in self.__controller.list_houses:
            # 直接打印对象,由对象的__str__方法决定打印风格
            print(house)

    def __show_house_by_max_total_price(self):
        house = self.__controller.get_house_by_max_total_price()
        print(house)

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
