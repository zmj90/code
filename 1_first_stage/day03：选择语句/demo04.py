"""
    真值表达式
        if 数据:
            语句
        本质就是使用bool函数操作数据

    if 真值表达式
        if 变量:
            如果有值则执行当前代码
        作用：可以简洁的判断变量是否有值

    条件表达式
        变量 = 满足条件的值 if 条件 else 不满足条件的值
        根据条件对某个变量进行赋值
    练习:exercise07.py
    17:10
"""

# 1. 真值表达式
if "a":
    # if bool("a"):
    print("真值")

str_input = input("请输入：")
if str_input:
    print("输入的字符串不是空的")
# 2.  条件表达式:有选择性的为变量进行赋值
# sex = None
# if input("请输入性别:") == "男":
#     sex = 1
# else:
#     sex = 0
# print(sex)
sex = 1 if input("请输入性别:") == "男" else 0
print(sex)

sex = 1 if input("请输入性别:") == "男" else None
print(sex)













