"""
    命名关键字形参
"""


# 要求必须用关键字实参传递
# 语法1:def 函数名(*args,命名关键字形参)
def func01(*args, p1=0):
    print(args)
    print(p1)


# 语法2:def 函数名(*,命名关键字形参)
def func02(*, p1):
    print(p1)


func01(p1=10)
func01(1, 2, 3, p1=10)
func01(1, 2, 3)
func02(p1=10)

# 应用
# def print(*values,sep=" ",end ="\n")
print("我是", "彭文韬", "今年", 23, "岁了", sep="")
print("*", end=" ")
