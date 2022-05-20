from json import load
from pipes import Template
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NewUserForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login 


# from .models import Task

def index (request):
    print(request.user)
    return render(request,'index.html')

def courses (request):
    return render(request,'courses.html')

# def register(request):
#     form= UserCreationForm()
#     return render(request,'accounts/register.html')

class RegisterPage(FormView):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('accounts/login')

    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

def login (request, user):
    return render(request,'accounts/login.html')

def liveqa (request):
    return render(request, 'liveqa.html')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name= 'accounts/profile.html'

