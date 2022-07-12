"""
    while 循环
        延长程序生命
        while True:
            循环体
            if 退出条件:
                break
"""
while True:
    sex = input("请输入性别:")
    if sex == "男":
        print("您好先生")
    elif sex == "女":
        print("您好女士")
    else:
        print("性别未知")

    if input("请输入q键退出:") == "q":
        break
# 练习:让下列代码重复执行，输入y继续(不输入y则退出)