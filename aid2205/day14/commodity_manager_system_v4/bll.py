from model import CommodityModel


class CommodityController:
    def __init__(self):
        self.__start_id = 1001
        self.list_commodity = []

    def add_commodity(self, new):
        """
            添加商品信息(设置商品编号,追加到列表中)
        :param new: CommodityModel类型,在view中录入的商品信息
        """
        new.cid = self.__start_id
        self.__start_id += 1
        self.list_commodity.append(new)

    def remove_commodity(self, cid):
        """
            在列表中移除学生信息
        :param cid: int类型,学生编号
        :return: bool类型,是否成功移除
        """
        if cid in self.list_commodity:
            self.list_commodity.remove(cid)
            return True
        return False

    def update_commodity(self, model):
        """

        :param model:
        :return:
        """
        for item in self.list_commodity:
            if item.cid == model.cid:
                item.__dict__ = model.__dict__
                return True
        return False

# 如果当前模块是主模块,才执行测试代码
# (如果项目发布后,在main.py启动,不执行当前代码)
if __name__ =="__main__":
    controller = CommodityController()
    controller.add_commodity(CommodityModel())
    controller.add_commodity(CommodityModel())
    controller.add_commodity(CommodityModel())
    for item in controller.list_commodity:
        print(item)