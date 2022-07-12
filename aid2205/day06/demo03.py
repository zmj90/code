"""
    以容器的思想(统一管理数据),改造下列代码
"""

month = int(input("请输入月份："))
if 1 <= month <= 12:
    if month == 2:
        print("29天")
    # elif month == 4 or month == 6 or month == 9 or month == 11:
    elif month in (4, 6, 9, 11):
        print("30天")
    else:  # 1 3 5 7 8 10 12
        print("31天")
else:
    print("输入有误")

tuple_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
print(tuple_days[0])  # 1月
print(tuple_days[2])  # 3月
print(tuple_days[month - 1])  # month月
