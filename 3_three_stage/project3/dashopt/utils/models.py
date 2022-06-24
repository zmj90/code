from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField("创建时间", auto_now_add=True)
    updated_time = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        # 制定当前模型类为抽象模型类
        # 特点 1、该模型类不会有对应的表
        # 特点 2、该模型类可被继承，当前字段一并被继承

        abstract = True
