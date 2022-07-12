"""
    字典推导式
"""
list_name = ["王利花", "张盼盼", "王万元"]
list_age = [33, 23, 28]
# dict_data = {}
# for i in range(len(list_name)):
#     key = list_name[i]
#     value = list_age[i]
#     dict_data[key] = value
dict_data = {list_name[i]:list_age[i]
             for i in range(len(list_name))}
print(dict_data)
# 练习1： 将两个列表，合并为一个字典
# 练习2： 颠倒练习1字典键值