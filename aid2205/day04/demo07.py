"""
    索引
        定位单个元素
        容器名[整数]
"""
message = "我是花果山水帘洞美猴王孙悟空"
print(message[0]) # 我
print(message[4]) # 山
print(message[-3]) # 山
# IndexError: string index out of range
# print(message[99])
# print(message[-99])
print(len(message)) # 长度14
# 定位中间元素
index = len(message) // 2
print(message[index])