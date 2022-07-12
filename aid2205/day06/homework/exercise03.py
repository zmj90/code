"""
    在终端中录入疫情地区名称，如果输入空字符串，则停止。
    如果录入的名称已经存在不要再次添加.
    最后倒序打印所有省份名称(一行一个)
"""
list_regions = []
while True:
    region = input("请输入疫情地区名称：")
    if region == "":
        break
    if region in list_regions:
        print("已经存在")
    else:
        list_regions.append(region)

# len(list_regions) - 1:从总数-1的位置开始
# -1：不包含-1,实际包含0(第一个位置)
# -1：倒序
for i in range(len(list_regions) - 1, -1, -1):
    print(list_regions[i])


"""
# 搞清range与切片的区别
list_regions = ["北京","上海","深圳"]
# 结束值-1：指的是数轴中的-1,不包含-1,包含0
for i in range(len(list_regions) - 1, -1, -1):
    print(list_regions[i])
# 结束值-1：指的是列表最后一个元素
for item in list_regions[len(list_regions)-1:-1:-1]:
    print(item)
"""