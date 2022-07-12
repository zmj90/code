"""
    list --> str
"""
list01 = ["a", "b", "c"]
result = "-".join(list01)
print(result) # a-b-c

# 需求:根据条件循环拼接字符串
# str_result = ""
# for number in range(10):
#     # 每次循环,+=都会产生新数据,旧数据成为垃圾
#     str_result += str(number)
# print(str_result) # 0123456789

# 解决:将不可变数据改为可变数据
list_result = []
for number in range(10):
    list_result.append( str(number) )
result = "".join(list_result)
print(result)
# 练习：
# 在终端中,循环录入字符串,如果录入空则停止.
# 停止录入后打印所有内容(一个字符串)