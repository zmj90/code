"""
    列表常用操作
        3.定位
        4.遍历
"""
list_name = ["李杨", "彭文韬", "王万元"]
# 3.定位:  容器名[索引/切片]
# -- 读取列表元素     ? = 容器名[索引/切片]
print(list_name[0])
# 通过切片读取数据,会创建新列表
print(list_name[-2:])

# -- 修改列表元素     容器名[索引/切片] = ?
list_name[1] = "spring"
# 通过切片修改数据,将右侧可迭代对象的元素依次存入左侧
list_name[:2] = ["老李", "老彭"]
# list_name[:2] = 10
list_name[:2] = "10"
print(list_name)

# 4.遍历
list_name = ["李杨", "彭文韬", "王万元"]
# 根据条件灵活的读取元素
# 需求:查找姓名是三个字的名称
for item in list_name:
    if len(item) == 3:
        print(item)

# 需求:将三个字的姓名改为两个字
# for item in list_name:
#     if len(item) == 3:
#         item = item[-2:] # 修改变量item与列表无关
#         print(item)
for i in range(len(list_name)):  # 0 1 2
    if len(list_name[i]) == 3:
        list_name[i] = list_name[i][-2:]
print(list_name)

# 需求:倒序读取每个元素
# for item in list_name[::-1]: # 不建议:会创建新列表
#     print(item)

# 2 1 0
# for i in range(2,-1,-1):
for i in range(len(list_name) - 1, -1, -1):
    print(list_name[i])
