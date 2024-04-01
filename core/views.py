from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *


def registerUser(request):
    

    if request.method == 'POST':
        data = request.POST 
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if password != confirm_password:
            messages.error(request,'Password didnt matched')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request,'Username already exist')
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.error(request,'Email already exist')
            return redirect('register')
        
        else:
            user=User.objects.create(
                username=username,
                email=email,
            )
            user.set_password(password)
            user.save()
            messages.success(request,'Account successfully created')
            return redirect('register')

        

    return render(request,'core/register.html')

def loginUser(request):
    if request.method=='POST':
        data=request.POST
        username=data.get('username')
        password = data.get('password')
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Loged in successfully')
            return redirect('login')
        
        elif user is None:
            messages.error(request,"User doesnt exist...")
        else:
            messages.error('Invalid credential')
            return redirect('homepage')
    return render(request,'core/login.html')


def homePage(request):
    dessert = Dessert.objects.all()

    if request.method == 'POST':
        order = Order.objects.create(customer=request.user)
        orderedItems = []
        totalPrice = 0
        for dessert_id, quantity in request.POST.items():
            if dessert_id.isdigit():
                dessert = Dessert.objects.get(pk=dessert_id)
                orderedItem = OrderedItem.objects.create(order=order, dessert=dessert, quantity=quantity)
                orderedItems.append(orderedItem)
                totalPrice += orderedItem.totalPrice()
        return render(request, 'orderSuccessful.html', {'orderedItems': orderedItems, 'totalPrice': totalPrice})
    return render(request,'homepage.html',{'dessert':dessert})

def logoutUser(request):
    logout(request)
    return redirect('login')

