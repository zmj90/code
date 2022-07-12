"""
    路径对象操作
        创建目录
            路径对象.mkdir()
        重命名
            路径对象.rename(新名称)
        删除
            文件路径对象.unlink()
            目录路径对象.rmdir()
"""
from pathlib import Path

# 1. 创建目录
# 目录不存在时创建,存在时报错
# Path("test").mkdir()
# 目录不存在时创建,存在时不报错
# Path("test").mkdir(exist_ok=True)
# 不能创建多级目录
# Path("test","dir01","dir02").mkdir()

# 2. 路径重命名
# Path("test").rename("Test")
# # Path("day18","homework","game2048").rename("Game2048")
# path = Path("day17", "homework")
# # # 路径对象.with_name() 保留路径只修改文件名
# path.rename( path.with_name("Homework")   )

# 3. 路径删除
# 目录必须为空，才能删除
Path("Test","a.py").unlink()
Path("Test").rmdir()


