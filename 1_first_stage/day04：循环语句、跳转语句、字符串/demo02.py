"""
    for: 适合执行预定次数。
    while:适合根据条件循环执行。
    练习:exercise05.py
        exercise06.py
        exercise07.py
"""

# for 变量 in 可迭代对象:
#     循环体

str01 = "我叫苏大强!"

# item 存储的是字符串中每个字符的地址
for item in str01:
    print(id(item))

# 整数生成器:  range(开始值,结束值,间隔)
# for + range ：　更善于执行预定次数。
for item in range(5):#01234
    print(item)

# 需求：折纸１０次
thickness = 0.0001
for item in range(10):
    thickness*=2
print(thickness)


"""
    for 循环
        for 变量名 in 容器:
            循环体

    while：根据条件重复
        经典案例：折纸到珠穆朗玛峰的高度

    for：适合获取容器中的元素
        for + range：根据次数重复
        经典案例：累加1到100之间的整数

    练习:exercise02
"""
message = "我是齐天大圣孙悟空"
# for item in message:
#     print(item)

for item in message:
    item = "圣"  # 修改循环变量,没有修改字符串中的字符
print(message)

# 在字符串中查找某个文字,如果存在打印该文字,不存在提示"没找到"
# name = "我是齐天大圣孙悟空"
# for item in name:
#     if item == "圣":
#         print(item)
#         break
# else:
#     print("没找到")
"""
    for + range
        整数生成器
    练习:exercise03
"""
# 不包含终点
# 写法1：range(起点,终点,间隔)
for item in range(1, 10, 1):
    print(item)  # 1 2 .... 9
# 写法2：range(终点)
for item in range(6):
    print(item)  # 0 1 2 .. 5
# 写法3：range(起点,终点)
for item in range(3, 9):
    print(item)  # 3 4 ... 8
