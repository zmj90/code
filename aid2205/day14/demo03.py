"""
    时间模块
"""
import time

# 人类时间
# 1.时间元组(年,月,日,时,分,秒,星期,年的第几天,夏令时偏移)
# 公园元年~2022年6月17日 14:22
# 秦始皇统一中国:-221
tuple_time = time.localtime()
print(tuple_time[2])  # 日
print(tuple_time[-3])  # 星期
print(tuple_time[:3])  # 年,月,日
print(tuple_time[3:-3])  # 时,分,秒

# 机器时间
# 2.时间戳
# 1970年元旦~1655447255.0960138(现在经过的秒数)
print(time.time())

# 3. 时间戳 --> 时间元组
# 语法:时间元组 = time.localtime(时间戳)
print(time.localtime(1655447255.0960138))
# 4. 时间元组 --> 时间戳
# 语法:时间戳 = time.mktime(时间元组)
print(time.mktime(tuple_time))

# 5. 时间元组 ->  字符串
# 语法：字符串 = time.strftime(格式, 时间元组)
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))
# 2022/06/17 14:46:18
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))
# Windows不支持中文格式化,Linux支持
# print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", tuple_time))
# 6. 字符串 -> 时间元组
# 语法：时间元组time.strptime(字符串,格式)
print(time.strptime("2022/06/17 14:46:18","%Y/%m/%d %H:%M:%S"))

