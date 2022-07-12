"""
    将列表中的数字累减
        list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
    结果：806400
"""
list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]

for item in list02:
    print(item)

# 从头到尾修改
# for i in range(len(list02)):
# 从第二个元素开始到末尾
# for i in range(1 , len(list02)):
# 倒序
# for i in range( len(list02)-1 , -1，-1):

result = list02[0] # 5
for i in range(1, len(list02)):
    result -= list02[i]
print(result)
