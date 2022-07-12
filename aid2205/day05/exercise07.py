"""

"""
import copy

list01 = ["北京", ["上海", "深圳"]]
list02 = list01  # 赋值:传递列表地址(数据1份)
list03 = list01[:]  # 浅拷贝:传递新列表地址(第一层数据2份,深层数据1份)
list04 = copy.deepcopy(list01)  # 深拷贝:传递新列表地址(数据2份)
list04[0] = "北京04"
list04[1][1] = "深圳04"
print(list01)  # ? 互不影响

list03[0] = "北京03"  # 修改第一层
list03[1][1] = "深圳03"  # 修改深层
print(list01)  # 深圳03

list02[0] = "北京02"
list02[1][1] = "深圳02"
print(list01)  # ? 都影响
