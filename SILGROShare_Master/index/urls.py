from django.contrib import admin
from django.urls import path,include
from . import  views#important

urlpatterns = [
    path('', views.index),
    #添加带有字符类型，整形，和slug的类型变量的URL
    path('<year>/<int:month>/<slug:day>',views.mydate),#变量名为year,month,day
    #这里也可以用正则表达式来限制变量的范围

    #下载文件
    path('download.html',views.download),
    #newListing
    path('newListing.html',views.newListing)

]