from django.db import models


class BaseModel(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        #指定当前模型类为抽象模型类
        #特点：1，该模型类不会有对应的表；2，其他模型类可继承该类，继承后，当前字段一并被继承
        abstract = True







