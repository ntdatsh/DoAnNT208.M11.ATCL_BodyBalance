from django import http
from django.contrib import auth
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from catagories.models import Product, PT, Exercise, whey
from .cart import Cart

from django.shortcuts import get_object_or_404

# Create your views here.

def get_index(request):
    return render(request, 'index.html')

class registerUser(View):
    def get(self, request):
        return render(request, 'register.html') 

    def post(self, request):
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password']
        password2= request.POST['password_confirmation']
        firstname= request.POST['firstname']
        lastname= request.POST['lastname']
        age= request.POST['age']
        gender= request.POST['gender']
        address= request.POST['address']
        user= User.objects.create_user(username,email,password1)
        user.save()
        return render(request, 'login.html')

class loginUser(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username= request.POST['username']
        password= request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        # Redirect to a success page.
            return render(request, 'indexafterlogin.html')
        else:
        # Return an 'invalid login' error message.
            return render(request, 'login.html')

def get_cart(request):
    cart = Cart(request)
    print(cart)
    return render(request, 'cart.html', {"cart": cart}) 

class pro(View):
    def get(self, request): 
        products = Product.objects.all()
        exercises = Exercise.objects.all()
        PTs = PT.objects.all()
        return render(request, 'MonitorBMI.html', {'products':products, 'exercises':exercises, 'PTs':PTs})

    def post(self, request):
        cart = Cart(request)
        if request.POST.get("action") == "post":
            product_id = int(request.POST.get("pr_id"))
            product_qty = int(request.POST.get("productqty"))
            cart.add(product = product_id, qty=product_qty)
            cartqty = cart.__len__()
            response = JsonResponse({"qty": cartqty})
            return response

def cartadd(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("productid"))
        product_qty = int(request.POST.get("productqty"))
        # cart.add(product = product_id, qty=product_qty)
        whey1 = get_object_or_404( whey, whey_id= product_id)
        cart.add(product= whey1, qty=product_qty)
        # cartqty = cart.__len__()
        # pro_id = int(request.POST.get("proid"))
        # pro_qty = int(request.POST.get("proqty"))
        # pro1 = get_object_or_404( Product, pr_id= pro_id)
        # cart.add(product= pro1, qty=pro_qty)

            # pt1 = get_object_or_404( PT, whey_id= product_id)
            # cart.add(product= pt1, qty=product_qty)
        cartqty = cart.__len__()
        response = JsonResponse({"qty": cartqty})
        return response

def cartadd1(request):
    cart = Cart(request)
    if request.POST.get("action") == "post":
        # product_id = int(request.POST.get("productid"))
        # product_qty = int(request.POST.get("productqty"))
        # cart.add(product = product_id, qty=product_qty)
        # whey1 = get_object_or_404( whey, whey_id= product_id)
        # cart.add(product= whey1, qty=product_qty)
        # cartqty = cart.__len__()
        pro_id = int(request.POST.get("proid"))
        pro_qty = int(request.POST.get("proqty"))
        pro1 = get_object_or_404(Product, pr_id= pro_id)
        cart.add1(product1= pro1, qty=pro_qty)
            # pt1 = get_object_or_404( PT, whey_id= product_id)
            # cart.add(product= pt1, qty=product_qty)
        cartqty = cart.__len__()
        response = JsonResponse({"qty": cartqty})
        return response

def logoutUser(request):
    logout(request)

def get_whey(request):
    return render(request,'WheyProtein.html')

def get_nutri(request):
    return render(request, 'Nutrition.html')

def get_PT(request):
    return render(request, 'PTRental.html')

def get_schedule(request):
    return render(request, 'Schedule.html')

def get_train(request):
    return render(request, 'TrainingPlan.html')

def get_indexafterlogin(request):
    return render(request, 'indexafterlogin.html') 

def get_checkout(request):
    return render(request, 'checkout.html')

# def products(request):
#     products = Product.objects.all()
#     print(products)
#     return render(request, 'MonitorBMI.html', {'products':products})
    
# def exercises(request):
#     exercises = Exercise.objects.all()
#     print(exercises)
#     return render(request, 'MonitorBMI.html', {'exercises':exercises})

# def PTs(request):
#     # products = get_object_or_404(Product, pr_id=1)
#     PTs = PT.objects.all()
#     print(PTs)
#     return render(request, 'MonitorBMI.html', {'PTs':PTs})

def wheys(request):
    # products = get_object_or_404(Product, pr_id=1)
    wheys = whey.objects.all()
    print(wheys)
    return render(request, 'WheyProtein.html', {'wheys':wheys})

def get_monitor(request):
    return render(request, 'MonitorBMI.html')



    
# def exercises(request):
#     exercises = Exercise.objects.all()
#     print(exercises)
#     return render(request, 'MonitorBMI.html', {'exercises':exercises})

# def PTs(request):
#     products = get_object_or_404(Product, pr_id=1)
#     PTs = PT.objects.all()
#     print(PTs)
#     return render(request, 'MonitorBMI.html', {'PTs':PTs})


