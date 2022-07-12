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
# 添加:字典名[键] = 值
dict_wlh["money"] = 100000000
# 2. 定位:字典名[键]
# --修改
dict_wlh["age"] = 36
# --读取
print(dict_wlh["sex"])
print(dict_wlh)
