"""

"""
dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}

# 获取字典第二个元素(键值对)
list_dict_data = list(dict_hobbies.items())
key = list_dict_data[1][0]
value = list_dict_data[1][1]
# 删除于谦第一个爱好
del dict_hobbies["于谦"][0]
# 删除郭德纲"唱"的爱好
dict_hobbies["郭德纲"].remove("唱")
# 修改字典key
dict_hobbies["大爷"] = dict_hobbies["于谦"]
del dict_hobbies["于谦"]






for item in dict_hobbies["于谦"]:
    print(item)

print(len(dict_hobbies["郭德纲"]))

for key in dict_hobbies:
    print(key)

for value in dict_hobbies.values():
    for item in value:
        print(item)
