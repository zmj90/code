"""
    数据访问层
"""
from pathlib import Path
from model import EpidemicModel

class EpidemicDao():
    """
        疫情信息数据访问对象
    """
    def __init__(self):
        self.__file_name = "epidemics.txt"
        Path(self.__file_name).touch(exist_ok=True)

    def save(self, list_data):
        """
            保存
        """
        with open(self.__file_name, "w", encoding="utf8") as file:
            for item in list_data:
                file.write(item.__repr__()+"\n")

    def load(self):
        """
            加载
        """
        list_data = []
        with open(self.__file_name, encoding="utf8") as file:
            for item in file:
                list_data.append(eval(item))
        return list_data
