from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def main(request):
    return render(request, 'tasks/start.html')


def Login(request):
    if request.method == 'POST':
        usname = request.POST.get("us_name")
        # email = request.POST.get("us_email")
        password_ = request.POST.get("name-password")
        try:
            user = User.objects.get(username= usname)
        except:
            messages.error(request, "User doesn't exist")
        user = authenticate(request, username=usname, password=password_)
        if user is not None:
            login(request, user)
            return redirect('notes')
        else:
            messages.error(request, "Wrong username or password")
    context = {}
    return render(request, 'tasks/log_reg.html', context)


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
