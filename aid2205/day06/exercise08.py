"""
    将第一行从左到右逐行打印

    将第二行从右到左逐行打印

    将第三列行从上到下逐个打印

    将第四列行从下到上逐个打印

    将二维列表以表格状打印
"""
list01 = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
]


# 00 01 02 03 04
# for c in range(5):
for c in range(len(list01[0])):
    print(list01[0][c])

# for item in list01[0]:
#     print(item)

# 14  13  12  11  10
for c in range(len(list01[1]) - 1, -1, -1):
    print(list01[1][c])

# 02  12  22
for r in range(len(list01)):
    print(list01[r][2])

# 23  13  03
for r in range(len(list01) - 1, -1, -1):
    print(list01[r][2])

# 00  01 02 03  04
# 10  11 12 13  14
# 20  21 22 23  24
for r in range(len(list01)):  #          0      1
    for c in range(len(list01[r])):  # 01234  01234
        print(list01[r][c], end="\t")
    print()

# for line in list01:
#     for item in line:
#         print(item,"\t")
#     print()