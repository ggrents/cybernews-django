from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView
from news.models import *
from django.core.paginator import Paginator

from .forms import *


class show_article(ListView):
    queryset = Article.objects.all()
    context_object_name = 'arts'
    template_name = 'index.html'
    paginate_by = 1


def addart(request):
    if request.method == 'POST':
        form = AddArticle(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('main-page')
    else:
        form = AddArticle()

    return render(request, 'addart.html', {'form': form})


def show_recent_article(request):
    arts = Article.objects.order_by('-created')[:3]
    cats = Category.objects.all()
    return render(request, 'index.html', {'arts': arts, 'cats': cats})


def show_only_category(request, slug):
    cats = Category.objects.all()
    chosen_category = Category.objects.get(slug=slug)
    arts = Article.objects.filter(category=chosen_category)
    return render(request, 'dotacat.html', {'articles': arts, 'cats': cats})


def article_detail(request, id):
    art = get_object_or_404(Article, pk=id)
    comments = Comment.objects.filter(article=art)
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(pk=id)
            comment.save()
            print("Комментарий добавлен!")
            return redirect('full-article', id=art.pk)
    else:
        form = AddComment()
    return render(request, 'detail.html', {'art': art, 'form': form, 'comments': comments})


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