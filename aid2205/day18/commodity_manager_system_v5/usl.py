from bll import CommodityController
from model import CommodityModel


class CommodityView:
    """
        界面视图:负责处理商品信息的输入/输出逻辑
    """

    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        """
            显示菜单
        """
        print("1键录入商品信息")
        print("2键显示商品信息")
        print("3键删除商品信息")
        print("4键修改商品信息")

    def __select_menu(self):
        """
            选择菜单
        """
        item = input("请输入选项:")
        if item == "1":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.__input_commodity()
        elif item == "2":
            # 难点1:本类多个方法互相调用
            # 通过self调用
            self.__display_commoditys()
        elif item == "3":
            self.__delete_commodity()
        elif item == "4":
            self.__modify_commodity()

    def __get_number(self,message):
        while True:
            try:
                number = int(input(message))
                return number
            except Exception:
                print("输入有误")

    def __input_commodity(self):
        """
            录入商品信息
        """
        # 难点2:跨类调用方式1(直接创建对象)
        model = CommodityModel()
        model.name = input("请输入商品名称:")
        # model.price = int(input("请输入商品单价:"))
        model.price = self.__get_number("请输入商品单价:")
        self.__controller.add_commodity(model)
        print("添加成功")

    def __display_commoditys(self):
        for item in self.__controller.list_commodity:
            # print(f"{item.name}的编号是{item.cid},单价是{item.price}")
            print(item)

    def __delete_commodity(self):
        # cid = int(input("请输入商品编号："))
        cid = self.__get_number("请输入商品编号：")
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        model = CommodityModel()
        # model.cid = int(input("请输入商品编号:"))
        model.cid = self.__get_number("请输入商品编号:")
        model.name = input("请输入商品名称:")
        model.price = self.__get_number("请输入商品单价:")
        if self.__controller.update_commodity(model):
            print("修改成功")
        else:
            print("修改失败")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()


