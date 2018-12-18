

from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse

from operation.models import Trolly, UserOrder
from users.models import UserProfile, Useradress
from goods.models import Goods
# Create your views here.




def add_trolly(request):
    if not request.session.get('userName', None):
        return render(request, "login.html")
    nick_name=request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    good_id = request.GET.get('good_id')

    good = Goods.objects.get(id=good_id)
    if request.method=="POST":
        num=request.POST.get('num')
        trolly_gd=Trolly(user=user,goods=good,num=num)
        trolly_gd.save()
    return render(request, 'detail.html', {'good': good, 'user': user})




def trolly(request):

    if not request.session.get('userName', None):
        return render(request, "login.html")
    nick_name=request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    if request.GET.get('type') == "add":
        good_id = request.GET.get('good_id')
        good = Goods.objects.get(id=good_id)
        good = Trolly.objects.get(goods=good,user=user)
        good.num=good.num+1
        if good.num>good.goods.num:
            good.num=good.num-1
        good.save()
    if request.GET.get('type') == "sub":
        good_id = request.GET.get('good_id')
        good = Goods.objects.get(id=good_id)
        good = Trolly.objects.get(goods=good, user=user)
        good.num = good.num - 1
        if good.num<0:
            good.num=0
        good.save()
    if request.GET.get('type') == "delete":
        good_id = request.GET.get('good_id')
        good = Goods.objects.get(id=good_id)
        good = Trolly.objects.get(goods=good, user=user)
        good.delete()
    goods_set=Trolly.objects.filter(user=user)
    total_num=0
    total_price=0
    for good in goods_set.values():
        gd=Goods.objects.get(id=good['goods_id'])
        total_price=total_price+good['num']*gd.price
        total_num=total_num+1
    return render(request, 'trolly.html', {'goods_set': goods_set, 'user': user,'total_price':total_price,'total_num':total_num})



def order(request):

    if not request.session.get('userName', None):
        return render(request, "login.html")
    nick_name=request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    goods_set = Trolly.objects.filter(user=user)
    total_num = 0
    total_price = 0
    flag=0
    for good in goods_set.values():

        gd = Goods.objects.get(id=good['goods_id'])

        total_price = total_price+good['num']*gd.price
        total_num = total_num + 1

        if request.GET.get('submit', None):
            new_order=UserOrder(goods=gd,state=0,price=gd.price*good['num'],buyer=user,adress=Useradress.objects.filter(user=user).last())
            new_order.save()
            flag=1
    if flag:
        return HttpResponseRedirect(reverse('home'))
    addrs = Useradress.objects.filter(user_id=user.id)

    return render(request, 'order.html',
                  {'goods_set': goods_set, 'user': user, 'total_price': total_price, 'total_num': total_num, 'addrs':addrs})

def delete_order(request):
    order_id=request.GET.get('order_id')
    order=UserOrder.objects.get(id=order_id)
    order.delete()
    return HttpResponseRedirect(reverse('user_order'))

