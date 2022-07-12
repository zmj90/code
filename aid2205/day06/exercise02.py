"""
    根据月日,计算是这一年的第几天.
    公式：前几个月总天数 + 当月天数
    例如：5月10日
    计算：31 29 31 30 + 10
"""
month = int(input("请输入月份："))  # 5
day = int(input("请输入天："))
tuple_days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# total_day = 0
# for i in range(month-1): # 0 1 2 3
#     total_day += tuple_days[i]
total_day = sum(tuple_days[:month - 1])
total_day += day
print(total_day)
