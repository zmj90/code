"""
    列表内存分布
        创建
        定位
"""
list_name = ["黎灯亮", "李杨", "李鹏宇"]
data01 = list_name
data02 = list_name[0]
data03 = list_name[:2]

data03[-1] = "杨杨"
data02 = "亮亮"
data01[-1] = "鹏鹏" # 影响list_name

print(list_name)
