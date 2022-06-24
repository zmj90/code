"""
    游戏 2048
        降维：将二维列表的操作，转换为对一维列表的操作.
            zero_to_end：对list_merge操作,将0元素移动到末尾
            merge：对list_merge操作,将非零元素、相邻且相同进行合并(向左移动的核心)
        每个函数职责单一：
            move_left：对list_map操作, 将二维列表每行数据交给merge处理(赋值给list_merge)
            move_right：对list_map操作, 将二维列表每行数据反向交给merge处理(赋值给list_merge)，最后反向还原
            move_up：对list_map操作, 矩阵转置,调用向左移动,矩阵转置
            move_down：对list_map操作, 矩阵转置,调用向右移动,矩阵转置
            matrix_transposition：对list_map操作,对角线不变，两端交换
            学习 -->  面试（销售）
"""
# 数据：全局变量
list_merge = [0, 0, 0, 0]
list_map = [
    [2, 0, 0, 2],
    [0, 2, 0, 2],
    [4, 0, 2, 2],
    [2, 0, 4, 4],
]

# 逻辑：函数
#  练习1:将零元素向后移动
#  [2, 0, 2, 0]  --> [2, 2, 0, 0]
#  [2, 0, 0, 2]  --> [2, 2, 0, 0]
#  [4, 2, 0, 8]  --> [4, 2, 8, 0]
# 写法1：forfor
def zero_to_end():
    """
        0元素移动到末尾
    """
    for i in range(len(list_merge) - 1):
        for r in range(i + 1, len(list_merge)):
            if list_merge[i] == 0:
                # 通过全局变量，修改指向的列表
                list_merge[i], list_merge[r] = list_merge[r], list_merge[i]

# 写法2：从后向前,删除0元素,追加0元素
# def zero_to_end():
#     # 在列表中删除多个元素,采用倒序删除
#     for i in range(len(list_merge) - 1, -1, -1):
#         if list_merge[i] == 0:
#             del list_merge[i]
#             list_merge.append(0)

#  练习2:合并相邻相同元素
#  [2, 0, 2, 0]  --> [2, 2, 0, 0] --> [4, 0, 0, 0]
#  [2, 0, 0, 2]  --> [2, 2, 0, 0] --> [4, 0, 0, 0]
def merge():
    """
        合并数据
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        # 如果 非零 且 相邻相同  则合并
        if list_merge[i] != 0 and list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

# 练习3：将list_map元素向左移动
def move_left():
    global list_merge
    for line in list_map:
        # 将list_map中每个元素(一维列表) 赋值给 全局变量(merge函数操作list_merge)
        list_merge = line
        merge()

# move_left()
# print(list_map)
# 练习4：将list_map元素向右移动
def move_right():
    global list_merge
    for line in list_map:
        list_merge = line[::-1]  # 反向切片，创建新列表
        merge()  # 向左逻辑操作新列表
        line[::-1] = list_merge  # 反向还原

# 练习5：将list_map元素向上、下移动
# 思路：将list_map进行矩阵转置
#      调用向左移动函数
#      将list_map进行矩阵转置

# 思路：将list_map进行矩阵转置
#      调用向右移动函数
#      将list_map进行矩阵转置
def matrix_transposition():
    # for r in range(1, len(list_map)):
    #     for c in range(r, len(list_map)):
    #         list_map[r - 1][c], list_map[c][r - 1] = list_map[c][r - 1], list_map[r - 1][c]
    for c in range(1, len(list_map)):
        for r in range(c, len(list_map)):
            list_map[r][c - 1], list_map[c - 1][r] = list_map[c - 1][r], list_map[r][c - 1]

# matrix_transposition()
# print("mt",list_map)


# 需求1：
# list_map[1][0]  <-->  list_map[0][1]
# list_map[2][0]  <-->  list_map[0][2]
# list_map[3][0]  <-->  list_map[0][3]
# 推导1：
# for r in range(1,4):
#    list_map[r][0] < -->  list_map[0][r]


#  需求2：
# list_map[2][1]  <-->  list_map[1][2]
# list_map[3][1]  <-->  list_map[1][3]
# 推导2：
# for r in range(2,4):
#    list_map[r][1]  <-->  list_map[1][r]

# 需求3：
# list_map[3][2]  <-->  list_map[2][3]
# 推导3：
# for r in range(3,4):
#   list_map[r][2]  <-->  list_map[2][r]

# 整理推导
# for r in range(1,4):
#    list_map[r][0] < -->  list_map[0][r]
# for r in range(2,4):
#    list_map[r][1]  <-->  list_map[1][r]
# for r in range(3,4):
#    list_map[r][2]  <-->  list_map[2][r]

# 继续推导：
# for c in range(1,len(list_map)):
#   for r in range(c,len(list_map)):
#       list_map[r][c-1] < -->  list_map[c-1][r]

def move_up():
    matrix_transposition()
    move_left()
    matrix_transposition()

def move_down():
    matrix_transposition()
    move_right()
    matrix_transposition()

# 执行
move_down()
print(list_map)
