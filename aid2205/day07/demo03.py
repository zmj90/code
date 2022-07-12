"""
    函数
"""

# 代码的重复就是万恶之源
"""
# 做(改) + 用
print("直拳")
print("摆拳")
print("勾拳")
print("侧踹")
# .....
# 做(改) + 用
print("直拳")
print("摆拳")
print("勾拳")
print("侧踹")
"""

# 做(变)
def attack(): # 菜谱
    print("直拳")
    print("摆拳")
    print("勾拳")
    print("侧踹")
    print("肘击")

# 用
# 调试F7进入函数,F8不进入
attack() # 开始炒菜
attack()

