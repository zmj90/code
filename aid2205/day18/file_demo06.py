"""
    二进制文件
"""
from pathlib import Path

name1 = Path("day17","装饰器.jpg")
name2 = Path("day17","装饰器2.jpg")
# 文件加密
with open(name1,"rb") as file_r:
    with open(name2,"wb") as file_w:
        content = file_r.read()
        file_w.write(b'ok') # 写入字节串(不是字符串)
        file_w.write(content)

name3 = Path("day17","装饰器3.jpg")
# 文件解密
with open(name2,"rb") as file_r:
    with open(name3,"wb") as file_w:
        # file_r.read(2) # 读取2个字节后丢弃
        file_r.seek(2) # 跳过2个字节
        content = file_r.read()
        file_w.write(content)

