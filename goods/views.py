from django.shortcuts import render

# Create your views here.
from users.models import UserProfile
from goods.models import Goods

dicts={'校园卡':1,'床位出租':2,'考研资料':3,'电子设备':4,'教材':5,'其他':6}

def upload_goods(request):
    if not request.session.get('userName',None):
        return render(request, "login.html")
    if request.method =="POST":
        name = request.POST.get('goodsname')
        detail_msg= request.POST.get('desc')
        type = request.POST.get('type')
        type = dicts[type]
        price = request.POST.get('price')
        state = 0
        num = request.POST.get('num')
        image = request.FILES.get('image')
        nick_name = request.session.get('userName')
        owner = UserProfile.objects.get(nick_name=nick_name)
        print(name,detail_msg,type,price,num,image,owner)
        if not all([owner, num, price , type, detail_msg,name]):
             return render(request, 'upload_goods.html', {'errmsg': '请将信息补充完整!'})
        try:
            if type==1:
                from_time = request.POST.get('from_time')
                to_time = request.POST.get('to_time')
                print(from_time,to_time)
                new_goods=Goods(name=name,desc=detail_msg,type=type,fromtime=from_time,totime=to_time,price=price,state=state,num=num,owner=owner)
            elif type==2:
                location = request.POST.get('location')
                new_goods = Goods(name=name,desc=detail_msg,type=type, location=location, price=price, state=state,num=num,owner=owner)
            else :
                new_goods = Goods(name=name,desc=detail_msg,type=type, price=price, state=state,num=num,owner=owner)
            if image!=None :
                new_goods.image=image
            new_goods.save()
        except Exception as e:
            print("e: ", e)  # 把异常打印出来
            return render(request, 'upload_goods.html', {'username':nick_name,'errmsg': '未知类型错误'})

            # 注册完，还是返回注册页。
        return render(request, 'upload_goods.html',{'username':nick_name})
    nick_name = request.session.get('userName')
    return render(request, 'upload_goods.html',{'username':nick_name})
def index(request):
    nick_name=request.session.get('userName',None)
    try:
        user = UserProfile.objects.get(nick_name=nick_name)
    except:
        user=None
    cards = Goods.objects.filter(type=1,num__gt=0)
    room = Goods.objects.filter(type=2,num__gt=0)
    postgraduate = Goods.objects.filter(type=3,num__gt=0)
    device= Goods.objects.filter(type=4,num__gt=0)
    teachingmeterial = Goods.objects.filter(type=5,num__gt=0)
    others = Goods.objects.filter(type=6,num__gt=0)
    return render(request,'index.html',
                  {'cards':cards,'room':room,'postgraduate':postgraduate,'device':device,'teachingmeterial':teachingmeterial,'others':others,'user':user})
def search(request):

    nick_name = request.session.get('userName', None)
    try:
        user = UserProfile.objects.get(nick_name=nick_name)
    except:
        user = None
    if request.method=="POST":
        msg=request.POST.get('msg')
        goods_set=Goods.objects.filter(name__contains=msg,num__gt=0)

        return render(request,'search.html',{'user':user,'goods_set':goods_set})
    type=request.GET.get('type')


    if type:
        type_s=type
        type=dicts[type]
        goods_set=Goods.objects.filter(type=type,num__gt=0)

        return render(request,'search.html',{'user':user,'goods_set':goods_set,'type':type_s})

    return render(request,'search.html',{'user':user})


def detail(request):
    nick_name = request.session.get('userName', None)
    try:
        user = UserProfile.objects.get(nick_name=nick_name)
    except:
        user = None
    good_id=request.GET.get('good_id')
    good=Goods.objects.get(id=good_id)
    return render(request,'detail.html',{'good':good,'user':user})

