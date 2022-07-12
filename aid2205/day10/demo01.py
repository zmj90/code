"""
    实例成员:对象.成员名
        实例变量
            语法：对象.变量名
        实例方法
            创建:
                def 方法名(self,参数):
                    方法体
            调用:
                对象.方法名(数据)
"""


class Wife:
    def __init__(self, name=""):
        # 创建实例变量
        self.name = name

    def work(self):
        print(self.name, "在工作")


jian_ning = Wife("建宁")  # jian_ning = {"name":"建宁"}
a_ke = Wife("阿科")  # a_ke = {"name":"阿科"}
# 修改实例变量
jian_ning.name = "公主"  # jian_ning["name"] ="公主"
# 读取实例变量
print(jian_ning.name)  # print(jian_ning["name"])
# 内置实例变量:存储自定义对象的实例变量名与值
print(jian_ning.__dict__)
# 使用自定义对象名
jian_ning.work()

# 建议:在类中创建实例变量
"""
class Wife:
    pass

jian_ning = Wife()
jian_ning.name = "建宁" # 只为当前对象添加实例变量
print(jian_ning.name) #

a_ke = Wife()
print(a_ke.name) # 不能使用"建宁"的实例变量
"""

# 建议：在__init__中创建实例变量
"""
class Wife:
    def set_name(self, name):
        self.name = name


jian_ning = Wife()
jian_ning.set_name("建宁")
print(jian_ning.name)  #
"""
