"""
    复习-MVC
        1. 学习目标：了解软件框架结构
            V:负责处理界面逻辑,例如:输入/输出
            C:负责业务逻辑处理,例如:添加/删除
            M:封装数据,例如:学生类型(学生姓名/年龄/成绩..)

        2. 需求
            输入信息,修改编号,存入列表.

        3. 代码
            class XXXModel:
                def __init__(self,data01=0,data02=0,id=0):
                    self.data01 = data01
                    self.data02 = data02
                    self.id = id

            class XXXView:
                def __init__(self):
                    self.controller = XXXController()

                def input_data(self):
                    model = XXXModel()
                    XXXModel.data01 = input()
                    XXXModel.data02 = input()
                    self.controller.add_data(model)

            class XXXController:
                def __init__(self):
                    self.start_id = 1001

                def add_data(self,new):
                    new.id = self.start_id
                    self.start_id += 1

            view = XXXView()
            view.input_data()
"""
