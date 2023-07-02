from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(("用户名"), max_length=50, unique=True)
    password = models.CharField(("密码"), max_length=50)
    created_time = models.DateTimeField(("创建时间"), auto_now_add=True)
    updated_time = models.DateTimeField(("更新时间"), auto_now=True)

    #print输出对象的格式?:
    def __str__(self) -> str:
        return 'username %s'%(self.username)
