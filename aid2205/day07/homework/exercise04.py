"""
	1. 打印北京的第一个景区

	2. 打印四川的第二个美食

	3. 所有城市 (一行一个)

	4. 北京所有美食(一行一个)

	5. 打印所有城市的所有美食(一行一个)
"""
dict_travel_info = {
    "北京": {
        "景区": ["长城", "故宫"],
        "美食": ["烤鸭", "豆汁焦圈", "炸酱面"]
    },
    "四川": {
        "景区": ["九寨沟", "峨眉山"],
        "美食": ["火锅", "兔头"]
    }
}
print(dict_travel_info["北京"]["景区"][0])
print(dict_travel_info["四川"]["美食"][1])
for key in dict_travel_info:
    print(key)
for item in dict_travel_info["北京"]["美食"]:
    print(item)
for value in dict_travel_info.values():
    for item in value["美食"]:
        print(item)
