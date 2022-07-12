"""
    dal 数据访问层
"""
from pathlib import Path
from model import CommodityModel


class CommodityDao:
    """
        商品数据访问对象
    """
    def __init__(self):
        self.file_name = "commodities.txt"
        # 如果没有txt文件,则创建
        Path(self.file_name).touch(exist_ok=True)

    def save(self,list_commodity):
        """
            保存
        """
        with open(self.file_name,"w",encoding="utf8") as file:
            for item in list_commodity:
                # model对象转换为字符串
                file.write(item.__repr__()+"\n")

    def load(self):
        """
            读取
        """
        list_commodity = []
        with open(self.file_name,encoding="utf8") as file:
            for item in file:
                # 字符串转换为model对象
                list_commodity.append(eval(item))
        return list_commodity