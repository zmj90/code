"""
    (3) 练习：在month01/day03目录中，分别使用绝对路径、相对路径与BASE.DIR路径判断下列文件是否存在：
    day03/demo01.py
    day03/homework/exercise01.py
    day04/homework/exercise01.py
"""
# 1.使用绝对路径
from pathlib import Path
# window
p1 = Path(r"C:\Users\QTX\Desktop\2205\code_2205\day03\demo01.py")
# linux
# p1 = Path(r"/home/tarena/PycharmProjects/pythonProject/demo01.py")
print("aaa",p1.exists())
# 2.相对路径
p2 = Path(r"../day03/demo01.py")
print(p2.exists())

# 3.BASE.DIR路径
import settings

p3 = settings.BASE_DIR.joinpath("day03", "demo01.py")
print("xxx",p3.exists()) # f