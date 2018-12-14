"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cmdb import views as vsindex
from operation import views as vsop
from goods import views as vsgoods
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

    path(r'index/', vsgoods.index, name='home'),
    path(r'login/', vsindex.login, name='login'),
    path(r'register/', vsindex.register, name='register'),
    path(r'uploadgoods/', vsgoods.upload_goods, name='uploadgoods'),
    path(r'search/', vsgoods.search, name='search'),
    path(r'detail/', vsgoods.detail, name='detail'),
    path(r'add_trolly/', vsop.add_trolly, name='add_trolly'),
    path(r'trolly/', vsop.trolly, name='trolly'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

