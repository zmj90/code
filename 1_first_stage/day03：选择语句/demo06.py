"""
    while 循环
        循环计数
            三大要素：开始值、结束值、增减量
            开始值
            while 对结束值的处理:
                循环体
                增减量
    while 计数
    练习：exercise09.py
"""

# 需求:执行三次

count = 0
while count < 3:  # 0  1  2
    count += 1
    usd = int(input("请输入美元："))
    print(usd * 6.9)


