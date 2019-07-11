from django.contrib import admin
from django.urls import path,include
from . import  views#important
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    #添加带有字符类型，整形，和slug的类型变量的URL
    path('<year>/<int:month>/<slug:day>',views.mydate),#变量名为year,month,day
    #这里也可以用正则表达式来限制变量的范围

    #下载文件
    path('download.html',views.download),
    #newListing
    path('newListing.html',views.newListing),
    #productPage
    path('productPage.html',views.productPage),
    #mountain bike
    path('mountain-bike.html',views.mountain_bike, name='mountain-bike'),
    #navbar
    path('navbar.html',views.navbar)

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)