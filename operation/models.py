import datetime

from django.db import models
#_*_coding:utf-8_*_
# Create your models here.
from users.models import UserProfile, Useradress
from goods.models import Goods

class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile,related_name=u"用户",on_delete=models.CASCADE)
    goods = models.ForeignKey(UserProfile,related_name=u"收藏商品",on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.time,verbose_name=u"添加时间")

    class Meta:
        verbose_name=u"用户收藏"
        verbose_name_plural=verbose_name

class UserOrder(models.Model):

    add_time = models.DateTimeField(default=datetime.time,verbose_name=u"添加时间")
    state = models.IntegerField(verbose_name=u"订单状态")

    price = models.FloatField(verbose_name=u"总价",default=0)
    adress = models.ForeignKey(Useradress,related_name=u"收货地址",on_delete=models.DO_NOTHING,default=u"")
    class Meta:
        verbose_name=u"订单"
        verbose_name_plural=verbose_name


class Usermessage(models.Model):

    fruser = models.ForeignKey(UserProfile,related_name=u"发送者",on_delete=models.CASCADE)
    touser = models.ForeignKey(UserProfile,related_name=u"接受者",on_delete=models.CASCADE)
    message = models.CharField(max_length=500,verbose_name=u"消息内容")
    hasread = models.BooleanField(default=False,verbose_name=u"是否已读")
    addtime = models.DateTimeField(default=datetime.time,verbose_name=u"发送时间")


    class Meta:
        verbose_name=u"用户消息"
        verbose_name_plural=verbose_name


class UserDemand(models.Model):
    name = models.CharField(max_length=15,verbose_name=u"需求商品名字")
    detail = models.CharField(max_length=200,verbose_name=u"详细描述")
    time = models.DateTimeField(default=datetime.time,verbose_name=u"添加时间")
    state = models.IntegerField(default=1,verbose_name=u"需求状态")
    user = models.ForeignKey(UserProfile,related_name=u"发起人",on_delete=models.CASCADE)
    state = models.ForeignKey(Goods,related_name=u"应征商品",on_delete=models.CASCADE)

    class Meta:
        verbose_name=u"用户需求"
        verbose_name_plural=verbose_name