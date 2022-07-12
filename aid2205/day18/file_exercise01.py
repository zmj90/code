"""
    当前文件存储在:month01中
    #(3) 练习：
    # -- 打印所有练习(名称为exercise)文件路径
    # -- 打印所有文本(.txt)文件路径的创建时间(格式：年/月/日)
"""
import time
from pathlib import Path

# 1.打印所有练习(名称为exercise)文件路径
# for item in Path.cwd().rglob("exercise*.py"):
#     # item 是路径对象
#     print(item.parts)

# 2.打印所有文本(.txt)文件路径的创建时间(格式：年/月/日)
for item in Path.cwd().rglob("*.txt"):
    # 时间元组 = time.localtime(时间戳)
    # 字符串 = time.strftime(格式, 时间元组)
    create_time = item.stat().st_ctime
    tuple_time = time.localtime(create_time)
    print(time.strftime("%Y/%m/%d", tuple_time))

# 扩展
# 将所有路径对象存入列表
all_file = list(Path.cwd().rglob("*"))
# 获取所有路径对象名称
print(list(map(lambda p: p.name, all_file)))
# 获取所有路径对象中的目录
print(list(filter(lambda p: p.is_dir(), all_file)))
