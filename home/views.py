from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,'home/home.html')
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def breakfast_check(request):
    return render(request,'breakfast_check.html')
def breakfast_menu(request):
    return render(request,'breakfast_menu.html')
def dinner_check(request):
    return render(request,'dinner_check.html')
def dinner_menu(request):
    return render(request,'dinner_menu.html')
def member(request):
    return render(request,'member.html')
def order_check(request):
    return render(request,'order_check.html')
def order(request):
    return render(request,'order.html')
def pay(request):
    return render(request,'pay.html')
def signup(request):
    return render(request,'signup.html')

