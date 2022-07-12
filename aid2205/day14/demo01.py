"""

"""

# "我过去"
# 语法：
#   import 模块名
#   模块名.成员名
# 原理：创建变量,关联目标模块地址
import module01

module01.func01()

# 你过来
# 语法：
#   from 模块名 import 成员
#   直接使用成员
# 原理：将目标模块中的成员加入到当前模块作用域中

# 注意1:如果导入的成员命名冲突,使用as创建别名
from module01 import func01 as f
from module01 import func02, func03

# 注意2：需要导入的成员过多,可以使用星号导入全部
from module01 import *

def func01():
    print("demo01-func01")

func01()
f()
