"""
    函数参数
        形式参数
"""

# 默认形参:允许实际参数不提供
def func01(p1="", p2=True, p3=0):
    print(p1)
    print(p2)
    print(p3)

# 位置形参:实际参数必须提供
def func02(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)

func01()
func01("a")
func01(p2 = False)
func01("a",p3 = 10)
