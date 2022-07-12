"""
    数据模型
"""
from typing import Optional


class HouseModel:
    """
        房源模型
    """

    def __init__(self, id: Optional[int] = 0, title: Optional[str] = "",
                 community: Optional[str] = "", years: Optional[str] = "",
                 house_type: Optional[str] = "", area: Optional[float] = 0.0,
                 floor: Optional[str] = "", description: Optional[str] = "",
                 total_price: Optional[float] = 0.0,
                 unit_price: Optional[float] = 0.0,
                 follow_info: Optional[str] = ""):
        """
            创建房源信息对象
        :param id:编号
        :param title: 标题
        :param community: 小区
        :param years:年份
        :param house_type:房型
        :param area:建筑面积
        :param floor:底层
        :param description:描述信息
        :param total_price:总价
        :param unit_price:单价
        :param follow_info:带看记录
        """
        self.id = id
        self.title = title
        self.community = community
        self.years = years
        self.house_type = house_type
        self.area = area
        self.floor = floor
        self.description = description
        self.total_price = total_price
        self.unit_price = unit_price
        self.follow_info = follow_info


    # 对象 -> 字符串(客户可看懂)
    def __str__(self):
        return f"{self.title}面积是{self.area}..."

    # 对象 -> 字符串(机器可识别)
    def __repr__(self):
        return f'HouseModel({self.id},"{self.title}","{self.community}","{self.years}","{self.house_type}",{self.area},"{self.floor}","{self.description}",{self.total_price},{self.unit_price},"{self.follow_info}")'

    # 对象最常用的比较大小逻辑(不灵活)
    def __gt__(self, other):
        return self.total_price > other.total_price
