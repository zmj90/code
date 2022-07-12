"""
    数据访问层
    data access layer
"""
from pathlib import Path
from typing import List

from model import HouseModel


class HouseDao:
    """
        房源数据访问对象
    """

    def __init__(self):
        self.__FILE_NAME = "house.txt"
        Path(self.__FILE_NAME).touch(exist_ok=True)

    def save(self, list_target) -> None:
        """
            保存房源信息
        """
        with open(self.__FILE_NAME, "w", encoding="utf-8") as file:
            for house in list_target:
                file.write(house.__repr__() + "\n")

    def load(self):
        """
            加载房源信息
        :return:文件中所有房源信息
        """
        list_house = []
        with open(self.__FILE_NAME, encoding="utf-8") as file:
            for row in file:
                list_house.append(eval(row))
        return list_house


if __name__ == '__main__':
    # 测试代码
    dao = HouseDao()
    list_target = dao.load()
    dao.save(list_target)
