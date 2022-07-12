"""
    函数内部修改传入的可变数据,
    无需使用return也能传递结果
"""


def func01(p1, p2):
    p1[0] = "彭彭"
    p2 = "虎子"

list01 = ["彭文韬"]
name = "樊威虎"
func01(list01, name)
print(list01)  # ?
print(name)  # ?
