from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Role(models.Model):
    color = models.CharField('职业颜色', max_length=100)
    name = models.CharField('职业名字',max_length=50, unique=True)
    Hp   = models.DecimalField('生命值',max_digits=20, decimal_places=2) #职业基础生命
    Mp  = models.DecimalField('魔法值',max_digits=20, decimal_places=2)  #职业基础#魔法值
    Level = models.IntegerField('等级')
    Damage = models.DecimalField('伤害值',max_digits=20, decimal_places=2)
    Defence =  models.DecimalField('防御值',max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name

class Hero(models.Model):
    name = models.CharField('名字',max_length=50, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Hp   = models.DecimalField('生命值',max_digits=20, decimal_places=2) #生命
    Mp  = models.DecimalField('魔法值',max_digits=20, decimal_places=2)  #魔法值
    Level = models.IntegerField('等级')
    Damage = models.DecimalField('伤害值',max_digits=20, decimal_places=2)
    Defence =  models.DecimalField('防御值',max_digits=20, decimal_places=2)

    def __str__(self):
        return self.name
