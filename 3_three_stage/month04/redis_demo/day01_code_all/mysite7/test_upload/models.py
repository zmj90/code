from django.db import models

# Create your models here.
class Content(models.Model):

    desc = models.CharField(max_length=100)
    #FileField只存储文件所在路径，不存储实际文件内容
    #实际内容存储在 MEDIA_ROOT + '/' + upload_to
    #models.ImageField - 专门负责存储图片
    myfile = models.FileField(upload_to='myfiles')