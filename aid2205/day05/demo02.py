"""
    列表常用操作
        5. 删除
"""
list_name = ["李杨", "彭文韬", "王万元"]
# -- 根据定位
# del list_name[1]
# del list_name[:2]
# del list_name[1], list_name[:2]
# -- 根据元素
list_name.remove("彭文韬")
# 如果不确定需要删除的元素存在,需要判断
if "spring" in list_name:
    list_name.remove("spring")
print(list_name)
