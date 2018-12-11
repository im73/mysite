#_*_coding:utf-8_*_
import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class UserProfile(AbstractUser):

    nick_name = models.CharField(max_length=15,verbose_name=u"昵称",null=False)
    gender =models.CharField(max_length=4,choices=(("male","男"),("female","女")),default="男")
    password = models.CharField(max_length=18,null=False,verbose_name=u"密码")
    mobile = models.CharField(max_length=11,null=False)
    major = models.CharField(max_length=20,null=False)
    image= models.ImageField(upload_to="image/%Y/%m",default=u"static/images/profile.png",max_length=100)
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    qq = models.EmailField(max_length=50, verbose_name=u"qq")
    grade = models.CharField(max_length=10,verbose_name=u"年级",default="大一")
    state = models.BooleanField(verbose_name=u"登陆状态",default=False)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.username

class Useradress(models.Model):

    mobile = models.CharField(max_length=11, null=False,verbose_name=u"手机号码")
    name = models.CharField(max_length=15, verbose_name=u"姓名", null=False)
    province = models.CharField(max_length=15, verbose_name=u"省名", null=False)
    city = models.CharField(max_length=15, verbose_name=u"城市", null=False)
    districts = models.CharField(max_length=15, verbose_name=u"地区", null=False)
    street = models.CharField(max_length=15, verbose_name=u"街道", null=False)
    detaile = models.CharField(max_length=100, verbose_name=u"详细地址", null=False)
    user = models.ForeignKey(UserProfile, verbose_name=u"用户", on_delete=models.CASCADE)
    class Meta:
        verbose_name=u"收货地址"
        verbose_name_plural=verbose_name

class EmailVerifyRecode(models.Model):
    code = models.CharField(max_length=20,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(max_length=10,choices=(("register","注册"),("forget",u"找回密码")))
    send_time= models.DateTimeField(default=datetime.time)
    class Meta:
        verbose_name=u"邮箱验证码"
        verbose_name_plural=verbose_name

class Banner(models.Model):
    title=models.CharField(max_length=100,verbose_name=u"标题")
    image=models.ImageField(upload_to="banner/%Y/%m",verbose_name=u"轮播",max_length=100)
    url=models.URLField(max_length=200,verbose_name=u"访问地址")
    index=models.IntegerField(verbose_name=u"图片顺序")
    add_time=models.DateTimeField(default=datetime.time,verbose_name=u"添加图片时间")
    class Meta:
        verbose_name=u"轮播图"
        verbose_name_plural = verbose_name