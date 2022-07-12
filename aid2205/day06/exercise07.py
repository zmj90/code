"""
    for循环画出下列图形
        外层循环4次   内层循环
        $             1
        $$            2
        $$$           3
        $$$$          4
"""
for r in range(4):#       0     1     2      3   r
    for c in range(r+1):# 0     01    012   0123
        print("$",end= "")
    print()

