"""
    行
"""
# 3个物理行  3个逻辑行
a = 10
b = 20
c = a + b

# 1个物理行  3个逻辑行(不建议)
a = 10;b = 20;c = a + b

# 3个物理行  1个逻辑行(不建议)
# 折行符
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
# (小中大)括号可以自动换行
b = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9) 
print(
    input("请输入职位:") == "高管"  or
    int(input("请输入年薪:")) > 500000
)
