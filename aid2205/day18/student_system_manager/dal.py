"""
    数据访问层
"""
from pathlib import Path

from model import StudentModel


class StudentDao:
    """
        学生数据访问对象
    """
    def __init__(self):
        self.file_name = "students.txt"
        # 手动创建文件
        # Path(self.file_name).touch(exist_ok=True)

    def save(self,list_student):
        """
            保存
        """
        with open(self.file_name,"w",encoding="utf8") as file:
            for item in list_student:
                file.write(item.__repr__()+"\n")

    def load(self):
        """
            加载
        """
        list_student = []
        with open(self.file_name,encoding="utf8") as file:
            for item in file:
                list_student.append(eval(item))
        return list_student
