from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Notation


class ListOfNotes(ListView):
    model = Notation
    context_object_name = "notes"


class Notice(DetailView):
    model = Notation
    context_object_name = "notice"


class CreateNotice(CreateView):
    model = Notation
    fields = '__all__'
    success_url = reverse_lazy("notes")
#     # context_object_name = "create-notice"


class UpdateNotice(UpdateView):
    model = Notation
    fields = '__all__'
    success_url = reverse_lazy("notes")

class DeleteNotice(DeleteView):
    model = Notation
    context_object_name = "notice"
    success_url = reverse_lazy("notes")
