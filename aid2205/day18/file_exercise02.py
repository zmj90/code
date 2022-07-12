"""
    练习：将每天homework.txt拷贝到backup/homeworks目录中，
     格式为:homework01~xx.txt
"""
from pathlib import Path
import shutil

# 1. 创建目录
Path("../backup").mkdir(exist_ok=True)
target_dir = Path("../backup", "homeworks")
target_dir.mkdir(exist_ok=True)
# 2. 获取所有文本文件
# enumerate 详见：day15/demo07.py
for i, item in enumerate(Path.cwd().rglob("homework.txt")):
    # 3. 拷贝(源文件,)
    # joinpath内部根据操作系统生成 / 或者 \
    shutil.copy(item, target_dir.joinpath(f"homework{i + 1:02}.txt"))
