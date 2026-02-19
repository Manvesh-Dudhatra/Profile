from django.shortcuts import render, redirect
from .models import CustomUser, Inquiry
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = CustomUser(username =username, email = email)
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, "auth/register.html")

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username = username, password = password)
        if not user:
            return redirect('login')

        login(request, user)
        return redirect('home')
    return render(request, 'auth/login.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        company = request.POST.get("company")
        address = request.POST.get('address')
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get('message')

        Inquiry.objects.create(name = f'{fname} {lname}', cname = company, address=address, email=email, phone=phone, message = message)

        return redirect('contact')
    return render(request, 'contact.html')

