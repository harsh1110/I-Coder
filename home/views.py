from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from shop.models import *

from .models import Blog

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        cart = order.objects.filter(user=request.user)
        total = 0
        for item in cart:
            total += int(item.product.price)
        param = {'cart':cart, 'bill':total}
        return render(request, 'home/homepage.html',param)
    else:
        return render(request, 'home.html')
    
def blogDetails(request,blog_id):
    blogpost = Blog.objects.get(blog_id = blog_id)
    cart = order.objects.filter(user=request.user)
    total = 0
    for item in cart:
        total += int(item.product.price)
    param = {'item':blogpost, 'cart':cart, 'bill':total}
    if request.user.is_authenticated:
        return render(request, 'home/blogDetails.html',param)
    else:
        return redirect('basehome')


def homePage(request):
    if request.user.is_authenticated:
        return render(request, 'home/homepage.html')
    else:
        return redirect('basehome')


def blog(request):
    blog = Blog.objects.all()
    cart = order.objects.filter(user=request.user)
    total = 0
    for item in cart:
        total += int(item.product.price)
    param = {'blog': blog, 'cart':cart, 'bill':total}
    if request.user.is_authenticated:
        return render(request, 'home/blog.html',param)
    else:
        return redirect('basehome')



def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.create_user(username=username, email=email, password=pass1)
        user.first_name = fname
        user.last_name = lname
        if pass1 != pass2:
            messages.error(request, "Passwords does not Matched")
            return redirect('basehome')
        elif username.isalnum() == False:
            messages.error(request, "Username Must In AlphaNumaric")
            return redirect('basehome')
        else:
            user.save()
            messages.success(request, "Succsessfully Registered Login To Access The Site!!")
            return redirect('home')
    else:
        return HttpResponse("404 - Not Found")






def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['loginusername']
        pass1 = request.POST['loginpass1']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "Succsessfully Logged In!!")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials, Please Try Again...")
            return redirect('basehome')
        
    else:
        return HttpResponse("404 - Not Found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Succsessfully Logged Out")
    return redirect('basehome')

