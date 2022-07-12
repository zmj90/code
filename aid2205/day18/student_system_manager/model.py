
class StudentModel:
    """
        学生模型:将多个学生信息封装为一个Model类型
    """

    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        # 全球唯一标识符(由controller决定)
        self.sid = sid

    def __str__(self):
        return f"{self.name}的编号是{self.sid},年龄是{self.age},成绩是{self.score}"

    # self是列表中的元素  other就是需要删除的sid
    def __eq__(self, other):
        return self.sid == other

    # 与str的区别是:__repr__转换为python代码形式的字符串
    def __repr__(self):
        return f'StudentModel("{self.name}",{self.age},{self.score},{self.sid})'