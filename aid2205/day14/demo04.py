"""
    包
    Python程序结构
    根目录
        包
            模块
                类
                    函数
                        语句
        settings.py
"""
# 导入路径：从项目跟目录开始
# 导入方式1
import package01.package02.module02 as m

m.func01()
m.func02()

# 导入方式2
from package01.package02.module02 import *

func01()
func02()
