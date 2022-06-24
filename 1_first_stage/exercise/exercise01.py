"""
    就是青蛙可以跳1台阶或者2台阶，问他跳n阶台阶有多少种方案
"""


def frog(n):
    if n in (1, 2):
        count = n
    else:
        count = frog(n - 1) + frog(n - 2)   # 跳最后一步时，要么是1台阶要么是2台阶。
    return count


print(frog(6))
