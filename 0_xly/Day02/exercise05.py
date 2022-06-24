# 打印以下数字
# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20

# 分析：
#   1、循环生成1-21之间的整数，不换行
#   2、如果当前数是5的倍数，则换行


# 1、循环生成1-21之间的整数，不换行
x = 1
while x < 21:
    print(x, end='\t')
    # 2、如果当前数是5的倍数，则换行
    if x % 5 == 0:
        print()
    x += 1

for x in range(1, 21):
    print(x, end='\t')
    if x % 5 == 0:
        print()



