# 1 打印整数： 0 3 6 9
# start:0  stop:10  step:3

# 2 打印整数： 5 4 3 2 1 0
# start:5  stop:-1  step:-1

# 3 打印整数： -5 -4 -3 -2 -1 0
# start:-5  stop:1  step:1

for i in range(0, 10, 3):
    print(i, end=' ')
print()  # 利用print的end默认'\n'

for i in range(5, -1, -1):
    print(i, end=' ')
print()

# 快捷输入：iter + Enter
for x in range(-5, 1):
    print(x, end=' ')
# print(end='\n')
