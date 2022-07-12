"""
    画出下列代码内存图
"""
name_of_beijing, region = "北京", "市"
# + 会产生新数据
name_of_beijing_region = name_of_beijing + region
region = "省"
print(name_of_beijing_region)  # ?
del name_of_beijing
print(name_of_beijing_region)  # ?

