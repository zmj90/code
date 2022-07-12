"""
    函数参数
        实际参数
"""
def func01(p1,p2,p3):
    print(p1)
    print(p2)
    print(p3)

# TypeError: func01() missing 1 required positional argument: 'p3'
# func01(1,2)
# TypeError: func01() takes 3 positional arguments but 4 were given
# func01(1,2,3,4)
# 1. 位置实参:根据顺序与形式参数进行对应
func01(1,2,3)
# 2. 关键字实参:根据名称与形式参数进行对应
func01(p2=2,p3=3,p1=1)
# TypeError: func01() got an unexpected keyword argument 'p4'
# func01(p2=2,p3=3,p1=1,p4 = 4)
