from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, FormView, CreateView
from news.models import *
from django.core.paginator import Paginator
from taggit.models import Tag

from .forms import *
from .forms import CreateUser



class SignUpView(View):
    form = CreateUser
    template_name = 'register.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main-page')
        return render(request, self.template_name, {'form': form})


class SignInView(View):
    template_name = 'login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        usname = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request, username=usname, password=passw)
        if user is not None:
            login(request, user)
            return redirect('main-page')
        else:
            return redirect('signin')


class Logout(LogoutView):
    next_page = 'main-page'


class PasswordChange(PasswordChangeView):
    success_url = reverse_lazy("main-page")
    template_name = "password_change_form.html"
