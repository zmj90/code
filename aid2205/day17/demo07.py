"""
    pathlib
"""
# 1. 创建路径
from pathlib import Path

# 不建议
# p1 = Path() # 当前路径的相对路径
# p2 = Path(r"C:\Users\QTX\Desktop\2205\code_2205") # 以绝对路径创建路径对象
# p3 = Path(r"..\\a.txt") # 以相对路径创建路径对象

p1 = Path.cwd() # 当前路径的绝对路径
p2 = Path.cwd().parent # 向上一层
# 向下一层
p3 = Path.cwd().joinpath("homework", "game2048.py")
print(p3.name)

# 在实际项目中如何使用路径?
import settings

p4 = settings.BASE_DIR.joinpath("day17", "demo01.py")
print(p4.name)

# 通过相对路径(如果相对关系改变,代码报错)
Path("demo01.py")
