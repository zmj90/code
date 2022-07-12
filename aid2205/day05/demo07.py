"""
    拷贝:防止数据被意外破坏
    浅拷贝:只复制一层
        优点:占用内存较少
        缺点:深层数据可能被破坏
        适用性:优先
    深拷贝:复制全部层
        优点:绝对互不影响
        缺点:占用内存较多
        适用性:深层数据可能被修改时
"""
list_name = ["黎灯亮", ["李杨", "李鹏宇"]]
data01 = list_name[:]  # 浅拷贝
data01[0] = "亮亮"
data01[1][1] = "鹏鹏"
print(list_name)  # ?

# 准备深拷贝工具
import copy

list_name = ["黎灯亮", ["李杨", "李鹏宇"]]
# 深拷贝
data01 = copy.deepcopy(list_name)
data01[0] = "亮亮"
data01[1][1] = "鹏鹏"
print(list_name)  # ?
