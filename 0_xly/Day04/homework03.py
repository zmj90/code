# 作业3：将字典中的键值对反向
# d = {'A':65, 'B':66, 'C':67}
# 结果为：{65:'A', 66:'B', 67:'C'}

d = {'A': 65, 'B': 66, 'C': 67}

dict_res = {}

for k, v in d.items():
    # print(k, v)
    dict_res[v] = k

print(dict_res)
