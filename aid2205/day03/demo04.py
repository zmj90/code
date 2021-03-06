"""
    选择语句
        让代码根据条件有选择性的执行

        写法1:
            if 条件:
                满足条件执行的代码
            ----------------------------
       写法2:
            if 条件:
                满足条件执行的代码
            else:
                不满足条件执行的代码
            ----------------------------
       写法3:
            if 条件1:
                满足条件1执行的代码
            elif 条件2:
                不满足条件1但满足条件2执行的代码
            else:
                以上条件都不满足执行的代码
            ----------------------------
    调试
       定义:让程序中断,逐语句执行,
           审查程序执行流程与变量取值.
       作用:
            1.看清程序执行过程,加强对程序的理解.
            2.排除代码错误
       步骤:
            1.加断点
            2.开始调试
            3.逐语句执行F8
"""
"""
sex = input("请输入性别:")
if sex == "男":
    print("您好先生")
else:
    print("您好女士")
"""
sex = input("请输入性别:")
if sex == "男":
    print("您好先生")
elif sex == "女":
    print("您好女士")
else:
    print("性别未知")