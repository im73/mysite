from django.http import HttpResponse
from django.shortcuts import render
from cmdb import models
from cmdb import db_con as con
# Create your views here.
def index(request):
    return render(request,"index.html")


def all_users(request):

    db = con.mysql_con()
    dicts=db.show_allusers()
    db.close_conn()

    return  render(request,"all_users.html",{"data":dicts})

def insert(request):
    db = con.mysql_con()
    if request.method=='POST':
        name = request.POST.get("name",None)
        stid = request.POST.get("stid",None)
        csnm = request.POST.get("csnm",None)
        grade = request.POST.get("grade",None)
        db.insert(name,stid,csnm,grade)
    db.close_conn()
    return render(request,"insert.html")



def delete(request):

    return  render(request,"delete.html")


def search(request):

    return  render(request,"search.html")



def modify(request):
    return  render(request,"modify.html")