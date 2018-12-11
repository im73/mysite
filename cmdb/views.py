from PIL import Image
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect,reverse

from cmdb import models
from cmdb import db_con as con
from users.models import UserProfile
import re
# Create your views here.


def all_users(request):

    db = con.mysql_con()
    dicts=db.show_allusers()
    db.close_conn()

    return  render(request,"all_users.html",{"data":dicts})


def register(request):
    if request.method=="POST":
        nick_name = request.POST.get('username')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        major = request.POST.get('major')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        qq = request.POST.get('qq')
        grade = request.POST.get('grade')
        password = request.POST.get('password')
        print(nick_name,gender,mobile,major,image,email,qq,grade,password)
        if not all([nick_name, gender, mobile , major, email,password]):
            # 有数据为空
            return render(request, 'register.html', {'errmsg': '必填项不能为空!'})

            # 判断邮箱是否合法
        if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            # 邮箱不合法
            return render(request, 'register.html', {'errmsg': '邮箱不合法!'})

            # 进行业务处理:注册，向账户系统中添加账户
            # Passport.objects.create(username=username, password=password, email=email)
        try:
            user=UserProfile(username=nick_name,nick_name=nick_name,gender=gender,mobile=mobile,major=major,image=image,email=email,qq=qq,password=password)
            if image!=None :
                user.image=image
            if grade!=None :
                user.grade=grade
            user.save()
        except Exception as e:
            print("e: ", e)  # 把异常打印出来
            return render(request, 'register.html', {'errmsg': '用户名已存在！'})

            # 注册完，还是返回注册页。
        return render(request, 'login.html', {'users': user})
    return render(request, 'register.html')

def login(request):
    if request.method=="POST":
        request.session.clear_expired()
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not all([username, password,]):
            # 有数据为空
            return render (request,"login.html",  {'errmsg': '用户名或密码为空'})
        users=UserProfile.objects.filter(nick_name=username,password=password)
        if users :
            request.session['userName'] = username
            return HttpResponseRedirect(reverse('home'))
        else:

            return render(request,"login.html",{'errmsg':'用户名或密码输入错误'})
    return render(request,"login.html",{'errmsg':None})

