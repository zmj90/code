"""
    搜索路径(文件,目录)
"""
from pathlib import Path

# 复习
# 当前目录的相对路径
# p1 = Path()
# print(p1)
# # 当前目录的绝对路径
# p2 = Path.cwd()

# 文件通配符
# 搜索 当前目录所有路径(一层)
# for item in Path.cwd().iterdir():
#     print(item)
# for item in Path("day03").iterdir():
#     print(item)
# 搜索 当前目录所有路径(根据通配符搜索一层)
# for item in Path.cwd().glob(r"day03\*.jpg"):
#     print(item)
# 递归 搜索当前目录所有路径(根据通配符搜索所有层)
for item in Path.cwd().rglob("*.jpg"):
    print(item)
