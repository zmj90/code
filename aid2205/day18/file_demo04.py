"""
    文件读写
"""

from pathlib import Path

name = Path("../day17", "homework.txt")
"""
# 1. 打开文件
file = open(name,encoding="utf8")
try:
    # 2. 读写文件
    print(file.read())
finally:
    # 3. 关闭文件
    file.close()
"""

# 1. 打开文件
# with：当cpu离开当前代码块时,自动调用close
with open(name, encoding="utf8") as file:
    # 2. 读写文件
    print(file.read())  # 读取全部内容(字符串)
    # print(file.readlines()) # 读取所有行(列表的每个元素就是一行)
    # for item in file: # 循环读取一行(省内存)
    #     print(item)
