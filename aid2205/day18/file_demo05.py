"""
    写入文件
"""
# 演示：写入简单数据
# with open("data01.txt","w",encoding="utf8") as file:
#     file.write("李佳辉\n")
#     file.write("王利花\n")

# 演示：写入自定义对象
class StudentModel:
    def __init__(self, name="", age=0, score=0, sid=0):
        self.name = name
        self.age = age
        self.score = score
        self.sid = sid

    def __str__(self):
        return f'StudentModel("{self.name}",{self.age},{self.score},{self.sid})'

ljh = StudentModel("李佳辉",28,100,101)

with open("../data01.txt", "w", encoding="utf8") as file:
    # file.write('StudentModel("李佳辉",28,100,101)\n')
    file.write(ljh.__str__())

# 演示：读取文件中的自定义对象
# ...
with open("../data01.txt", encoding="utf8") as file:
    for item in file:
        # 根据字符串执行python代码
        new = eval(item)
        print(new)