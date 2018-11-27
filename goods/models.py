from datetime import datetime
from time import timezone

from django.db import models
#_*_coding:utf-8_*_
# Create your models here.

from users.models import UserProfile
class Goods(models.Model):

    name = models.CharField(max_length=50,verbose_name=u"商品名称")
    desc = models.CharField(max_length=300,verbose_name=u"商品描述")
    type = models.IntegerField(verbose_name=u"商品种类")
    state = models.IntegerField(verbose_name=u"状态")
    fromtime = models.DateTimeField(verbose_name=u"开始时间")
    totime = models.DateTimeField(verbose_name=u"结束时间")
    release_time=models.DateTimeField(verbose_name=u"发布时间",default=datetime.now)
    price = models.FloatField(verbose_name=u"价格",null=False)
    location = models.CharField(max_length=100,verbose_name=u"地点")
    image = models.ImageField(upload_to="goods/%Y/%M",verbose_name=u"封面图",max_length=300)
    num = models.IntegerField(verbose_name=u"持有数量",default=1)
    owner = models.ForeignKey(UserProfile,verbose_name=u"拥有者",on_delete=models.CASCADE)

    class Meta:
        verbose_name=u"商品"
        verbose_name_plural = verbose_name

