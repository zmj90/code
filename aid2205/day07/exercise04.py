"""
    练习1：创建计算治愈比例的函数
    confirmed = int(input("请输入确诊人数:"))
    cure = int(input("请输入治愈人数:"))
    cure_rate = cure / confirmed * 100
    print("治愈比例为" + str(cure_rate) + "%")
"""
def calculate_cure_rate(confirmed, cure):
    """
        计算治愈比例
    :param confirmed: int类型,确诊人数
    :param cure:  int类型,治愈人数
    :return: float类型,治愈比例
    """
    cure_rate = cure / confirmed * 100
    return cure_rate

rate = calculate_cure_rate(130, 120)
print(rate)

cure_number = 100
confirmed_number = 110
rate = calculate_cure_rate( cure_number,confirmed_number)
print(rate)


