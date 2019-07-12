from django.contrib import admin
from django.urls import path,include
from . import  views#important
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homePage),
    #添加带有字符类型，整形，和slug的类型变量的URL
    path('<year>/<int:month>/<slug:day>',views.mydate),#变量名为year,month,day
    #这里也可以用正则表达式来限制变量的范围

    #下载文件
    path('download.html',views.download),
    #newListing
    path('newListing.html',views.newListing),
    #navbar
    path('navbar.html',views.navbar),

    path('create-account.html',views.createAccount),

    path('searchResult.html',views.searchResult),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)