# while死循环

# 需求：循环输入，当输入为空，则结束输入

# 将循环条件结果直接设置为True
while True:
    data = input('请输入：')

    if data == '':  # 为空
        break    # 结束输入

    print('输入的是', data)