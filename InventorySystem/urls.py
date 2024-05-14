"""InventorySystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from InventoryApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing,name='ln'),
    path('reg/',views.register,name='rgr'),
    path('log/',views.user_login,name='lgn'),
    path('log1/',views.user_login1,name='lgn1'),
    path('main/',views.mainpage,name='mn'),
    path('csh/',views.Cashier_page,name='cs'),
    path('abt/',views.about,name='ab'),
    path('pdt/',views.product,name='pd'),
    path('pdted/<int:pid>/',views.productedit,name='pded'),
    path('pdtdlt/<int:pid>/',views.productdelete,name='pddt'),
    path('ctg/',views.category,name='ct'),
    path('ctged/<int:cid>/',views.categoryedit,name='cted'),
    path('ctdlt/<int:cid>/',views.categorydelete,name='ctdlt'),
    path('viewcsh/<int:id>/',views.viewcashier,name='vcsh'),
    path('editcsh/<int:id>/',views.editcashier,name='ecsh'),
    path('delcsh/<int:id>/',views.deletecashier,name='dcsh'),
    path('list/',views.itemslist,name='list'),
    path('add/<int:id>/',views.adding,name='add'),
    path('minus/<int:id>/',views.removing,name='minus'),
    path('cart/',views.cart,name='cart'),
    path('hist/',views.history,name='hist'),
    path('button/',views.button,name='but'),
    path('viewcat/<int:id>/',views.viewcat,name='viewcat'),
    path('clist/',views.citemslist,name='clist'),
    path('cbutton/',views.cbutton,name='cbut'),
    path('ccart/',views.ccart,name='ccart'),
    path('cadd/<int:id>/',views.cadding,name='cadd'),
    path('cminus/<int:id>/',views.cremoving,name='cminus'),
]
