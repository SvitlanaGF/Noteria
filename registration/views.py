from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def main(request):
    return render(request, 'registration/start.html')


def Login(request):
    if request.method == 'POST':
        usname = request.POST.get("us_name")
        email = request.POST.get("us_email")
        password_ = request.POST.get("name-password")
        usr = authenticate(request, username=usname,email=email,password=password_)
        if usr is not None:
            Login(request)
            return HttpResponseRedirect('Success!')
    return render(request, 'registration/login.html')


def register(request):
    if request.method == 'POST':
        usname = request.POST.get("us_name")
        email = request.POST.get("us_email")
        password_ = request.POST.get("name-password")
        password_test = request.POST.get("name-password1")
        if password_ != password_test:
            return HttpResponseRedirect("Wrong password")
        usr = User.objects.create_user(username=usname, email=email, password=password_)
        usr.save()
        return redirect('login')
    return render(request, 'registration/register.html')

def Logout(request):
    logout(request)
    return request('main')