"""
        选择语句：运行时,根据某些条件决定是否执行语句

        缩进： 4个空格（在专业开发工具中,使用1个tab快捷键）
        if 语句
            if 条件:
                满足条件执行的代码
            else:
                不满足条件执行的代码
    练习:exercise01.py
        exercise02.py
        exercise03.py
        exercise04.py
        exercise05.py
        exercise06.py
"""

sex = input("请输入性别：")
if sex == "男":
    print("您好，先生！")
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知")

print("后续逻辑")

# 调试：让程序中断，逐语句执行。
#   　--　目的：审查程序运行时变量取值
#             审查程序运行的流程
#     --　步骤：
#            1. 加断点(可能出错的行)
#            2. 调试运行  Ｓｈｉｆｔ＋Ｆ９
#            3.  执行一行　F8
#            ４. 停止　Ctrl +F2

