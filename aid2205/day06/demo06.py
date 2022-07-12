"""
    字典基本操作
        创建
        添加
        定位
        遍历
        删除
"""
dict_wlh = {
    "name": "王利花",
    "age": 33,
    "sex": "女",
}
# 获取key
for key in dict_wlh:
    print(key)
# 获取value
for value in dict_wlh.values():
    print(value)
# 获取key和value
for k,v in dict_wlh.items():
    print(k)
    print(v) 
print(list(dict_wlh)) # ['name', 'age', 'sex']
print(list(dict_wlh.values())) # ['王利花', 33, '女']
print(list(dict_wlh.items())) # [('name', '王利花'), ('age', 33), ('sex', '女')]

# 删除:del 字典名[键]
del dict_wlh["sex"]
print(dict_wlh)