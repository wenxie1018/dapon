from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('index/',views.index),
    path('login/',views.login),
    path('breakfast_check/',views.breakfast_check),
    path('breakfast_menu/',views.breakfast_menu),
    path('dinner_check/',views.dinner_check),
    path('dinner_menu/',views.dinner_menu),
    path('member/',views.member),
    path('order_check/',views.order_check),
    path('order/',views.order),
    path('pay/',views.pay),
    path('signup/',views.signup),
]