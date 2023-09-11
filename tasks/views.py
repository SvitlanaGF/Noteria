from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Notation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def main(request):
    return render(request, 'tasks/start.html')

def Login(request):
    page = 'login'
    if request.method == 'POST':
        usname = request.POST.get("us_name").lower()
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
    context = {'page': page}
    return render(request, 'tasks/log_reg.html', context)

def register(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == 'POST':
        usname = request.POST.get("us_name")
        # email = request.POST.get("us_email")
        password_ = request.POST.get("name-password")
        password_test = request.POST.get("name-password1")
        # form = UserCreationForm(request.POST)
        if password_ != password_test:
            messages.error(request, "Different passwords")
        else:
            user = User.objects.create_user(username=usname.lower(), password=password_)
            return redirect('login')


    context = {'form': form, 'page': page}
    return render(request, 'tasks/log_reg.html', context)


# def Logout(request):
#     logout(request)
#     return redirect('main')



class ListOfNotes(LoginRequiredMixin, ListView):
    model = Notation
    context_object_name = "notes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        context['count'] = context['notes'].filter(complete=False).count()
        return context

class Notice(LoginRequiredMixin, DetailView):
    model = Notation
    context_object_name = "notice"


class CreateNotice(LoginRequiredMixin, CreateView):
    model = Notation
    fields = '__all__'
    success_url = reverse_lazy("notes")
#     # context_object_name = "create-notice"
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(CreateNotice, self).form_valid(form)


class UpdateNotice(LoginRequiredMixin, UpdateView):
    model = Notation
    fields = '__all__'
    success_url = reverse_lazy("notes")


class DeleteNotice(LoginRequiredMixin, DeleteView):
    model = Notation
    context_object_name = "notice"
    success_url = reverse_lazy("notes")
