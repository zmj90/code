"""
    时间处理
    练习：exercise01.py
         exercise02.py
"""
import time

# 1. 获取当前时间戳(从1970年1月1日到现在经过的秒数)
# 1560998261.108855
print(time.time())

# 2. 时间元组(年，月，日，时，分，秒，一周的第几天，一年的第几天，夏令时)
# 时间戳 --> 时间元组
print(time.localtime(1560998261))
# 通过元组的操作获取时间
tuple_time = time.localtime()
for item in tuple_time:
    print(item)
print(tuple_time[1])  # 获取月

# 通过类的操作获取时间
print(type(tuple_time))
# print(time.struct_time)
print(tuple_time.tm_year)  # 获取年

#  时间元组 --> 时间戳
print(time.mktime(tuple_time))

# 3. 时间元组 -->  str
str_time01 = time.strftime("%Y / %m / %d %H:%M:%S", tuple_time)
print(str_time01)

# str  -->  时间元组
print(time.strptime(str_time01, "%Y / %m / %d %H:%M:%S"))
