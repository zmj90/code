"""
创建函数,根据课程阶段计算课程名称.
number = input("请输入课程阶段数：")
if number == "1":
    print("Python语言核心编程")
elif number == "2":
    print("Python高级软件技术")
elif number == "3":
    print("Web全栈")
elif number == "4":
    print("项目实战")
elif number == "5":
    print("数据分析、人工智能")
"""


def computing_course_titles(number):
    """
        根据课程阶段数计算课程名称
    :param number: str类型,课程阶段数
    :return: str类型,课程阶段名称
    """
    dict_course_name = {
        "1": "Python语言核心编程",
        "2": "Python高级软件技术",
        "3": "Web全栈",
        "4": "项目实战",
        "5": "数据分析、人工智能",
    }

    # 如果字典key不存在,则报错.
    if number in dict_course_name:
        return dict_course_name[number]
    # else: # 函数默认返回None
    #     return None
title = computing_course_titles("10")
print(title)
