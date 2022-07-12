"""
    复习-MVC
        1. 学习目标：了解软件框架结构
            V:负责处理界面逻辑,例如:输入/输出
            C:负责业务逻辑处理,例如:添加/删除
            M:封装数据,例如:学生类型(学生姓名/年龄/成绩..)
        2. 语法
            class XXXController:
                def add_data(self,new):
                    pass

            class XXXModel:
                def __init__(self,data01):
                    self.data01 = data01

            class XXXView:
                def __init__(self):
                    self.controller = XXXController()

                def select_menu(self):
                    # 难点1:本类调用
                    self.input_data()

                def input_data(self):
                    # 难点2:跨类调用方法1
                    model = XXXModel()
                    model.data01 = input()

                    # 难点3:跨类调用方法2
                    self.controller.add_data(model)

            view = XXXView() # 执行__init__
            view.select_menu() #
"""