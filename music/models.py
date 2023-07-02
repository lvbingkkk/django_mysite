from django.db import models

# Create your models here.
class Books (models.Model):
    name = models.CharField('书名', max_length=100)
    price = models.DecimalField(("价格"), max_digits=7, decimal_places=2)
    author = models.CharField(("作者"), max_length=50)
    pub = models.CharField("出版社", max_length=100, default='')
    is_active = models.BooleanField("是否活跃", default=True)
