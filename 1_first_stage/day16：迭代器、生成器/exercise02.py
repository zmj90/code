# 练习2:不使用for，获取字典所有数据。
#  {"铁扇公主":101,"铁锤公主":102,“扳手王子”:103}
# 10:40

dict01 = {"铁扇公主": 101, "铁锤公主": 102, "扳手王子": 103}

iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
