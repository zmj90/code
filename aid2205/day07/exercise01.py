"""
    升序排列
"""
list01 = [4, 5, 5, 6, 7, 8, 89]
for r in range(len(list01) - 1):  # 0
    for c in range(r + 1, len(list01)):
        if list01[r] > list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
