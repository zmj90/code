"""
    面向对象
        思考流程
            现实世界             虚拟世界
            出租车 -抽象化->  类  -实例化->  对象
                          车牌号         京C007
                           颜色           白色
                           品牌           奔驰
"""


# 面向对象编程名
# 老婆类


class Wife:
    def __init__(self, name, height, face_score=80):
        # 数据
        self.name = name
        self.height = height  # 快捷键:alt+回车
        self.face_score = face_score

    # 行为
    def work(self):
        print(self.name, "在上班")


# 建宁对象
jian_ning = Wife("建宁", 168, 93)
jian_ning.work()# work(jian_ning)

# 阿轲对象
a_ke = Wife("阿轲", 170, 88)
a_ke.work()
