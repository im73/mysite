from django.shortcuts import render

from django.core.paginator import Paginator
# Create your views here.
from users.models import UserProfile
from users.models import Useradress
from operation.models import UserOrder
from goods.models import Goods

def user_info(request):
    nick_name = request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    return render(request,'user.html',{'user':user})

def user_order(request):

    nick_name=request.session.get('userName', None)
    page=request.GET.get('page')
    user = UserProfile.objects.get(nick_name=nick_name)
    order_li = UserOrder.objects.filter(buyer=user)

    # 遍历获取订单的商品信息
    # order->OrderInfo实例对象
    order_addr=0
    # for order in order_li.values():
    #     print(order)
    #     # 根据订单id查询订单商品信息
    #
    #     order.addr = Useradress.objects.get(id=order['adress_id'])
    #     order.goods = Goods.objects.get(id=order['goods_id'])

    paginator = Paginator(order_li, 3)  # 每页显示3个订单

    num_pages = paginator.num_pages

    if not page:  # 首次进入时默认进入第一页
        page = 1
    if page == '' or int(page) > num_pages:
        page = 1
    else:
        page = int(page)

    order_li = paginator.page(page)

    if num_pages < 5:
        pages = range(1, num_pages + 1)
    elif page <= 3:
        pages = range(1, 6)
    elif num_pages - page <= 2:
        pages = range(num_pages - 4, num_pages + 1)
    else:
        pages = range(page - 2, page + 3)

    context = {
        'order_li': order_li,
        'pages': pages,
        'user': user,
#        'addr': order_addr,
#        'goods': goods,
    }

    return render(request, 'user_order.html', context)

def user_address(request):
    nick_name = request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    addr_li=Useradress.objects.filter(user_id=user.id)
    context = {
        'addr_li': addr_li,
        'user': user,
    }
    return render(request, 'user_addr.html', context)

def add_address(request):
    nick_name = request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    if request.method == "POST":
        province = request.POST.get('province')
        city = request.POST.get('city')
        districts = request.POST.get('districts')
        street = request.POST.get('street')
        detaile = request.POST.get('detaile')
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        print(province, districts, city, street, detaile, name, mobile)
        if not all([province, districts, city, street, detaile, name, mobile]):
            # 有数据为空
            return render(request, 'addr_add.html', {'errmsg': '必填项不能为空!', 'user': user})
        try:
            addr=Useradress(mobile=mobile,name=name,province=province,city=city,districts=districts,street=street,detaile=detaile,user=user)
            addr.save()
        except Exception as e:
            print("e: ", e)  # 把异常打印出来
            return render(request, 'addr_add.html', {'errmsg': '用户名已存在！', 'user': user})
        return render(request, 'addr_add.html', {'addr': addr, 'user': user})
    return render(request, 'addr_add.html', {'user': user})

def user_good(request):
    nick_name = request.session.get('userName', None)
    user = UserProfile.objects.get(nick_name=nick_name)
    good_li = Goods.objects.filter(owner_id=user.id)
    context = {
        'good_li': good_li,
        'user': user,
    }
    return render(request, 'user_good.html', context)