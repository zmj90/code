"""
    容器综合训练
        for for
"""
"""
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print() # 换行
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print("*", end=" ")
print() # 换行
"""

"""
for c in range(5):
    print("*", end=" ")
print() # 换行

for c in range(5):
    print("*", end=" ")
print() # 换行
"""

# 外层执行1次,内层执行n次
for r in range(2):  # 0       1
    for c in range(5):  # 01234  01234
        print("*", end=" ")
    print()  # 换行
