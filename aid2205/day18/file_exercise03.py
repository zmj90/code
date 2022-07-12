"""
    练习：获取month01目录下所有python代码字符数
"""
from pathlib import Path

count = 0
for item in Path.cwd().rglob("*.py"):
    with open(item,encoding="utf8") as file:
        count += len(file.read())
print(count)