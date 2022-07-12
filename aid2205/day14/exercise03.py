"""
    练习1：定义函数,根据年月日,计算星期。
    输入：2020  9  15
    输出：星期二
"""
import time


def calculate_week_name(year, month, day):
    """
        计算星期名
    :param year:int类型年
    :param month:int类型月
    :param day:int类型日
    :return:str类型,星期名
    """
    # 参数 --> 字符串
    # str_time = "%s-%s-%s"%(year,month,day)
    str_time = f"{year}-{month}-{day}"
    # 字符串 --> 时间元组
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    # 时间元组 --> 星期数(012..)
    index = tuple_time[-3]
    # 星期数 --> 星期名(星期一...)
    tuple_week_name = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week_name[index]


print(calculate_week_name(2022, 6, 17))