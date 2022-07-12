"""
    打印台湾疫情信息(xx地区新增xx人现有xx人)
    将地区列表后2个元素修改为 ["ZJ","GX"]
    打印新增列表元素(一行一个)
    倒序打印现有列表元素(一行一个)
"""
list_region = ["台湾", "陕西", "浙江"]
list_new = [16, 182, 2]
list_now = [2339, 859, 505]
list_total = [16931, 1573, 2008]

print("%s地区新增%s人现有%s人" % (list_region[0], list_new[0], list_now[0]))
print(f"{list_region[0]}地区新增{list_new[0]}人现有{list_now[0]}人")

list_region[-2:] = ["ZJ","GX"]

for item in list_new:
    print(item)

# range(开始,结束,间隔)
# len(list_now)-1：从最后一个元素开始
# -1：不包含-1,包含0
# -1:倒序
for i in range(len(list_now)-1,-1,-1):# 2 1 0
    print(list_now[i])
