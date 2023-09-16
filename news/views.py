from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, FormView, CreateView
from news.models import *
from django.core.paginator import Paginator
from taggit.models import Tag

from .forms import *


class show_article(ListView):
    queryset = Article.objects.all()
    template_name = 'index.html'
    context_object_name = 'arts'
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


def show_article_byTags(request, tag):
    try:
        tag = Tag.objects.get(name=tag)
        arts = Article.objects.filter(tags=tag)
    except Tag.DoesNotExist:
        arts = Article.objects.none()
    cats = Category.objects.all()
    return render(request, 'index.html', {'arts': arts, 'cats': cats})


def addart(request):
    if request.method == 'POST':
        form = AddArticle(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user

            article.save()
            article.tags.set(form.cleaned_data['tags'])
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
    return render(request, 'index.html', {'arts': arts})


def article_detail(request, id):
    art = get_object_or_404(Article, pk=id)
    comments = Comment.objects.filter(article=art)
    tags = art.tags.all()
    similar_arts = Article.objects.filter(tags__in=tags).exclude(id=art.id).distinct()
    print()
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('signin')

        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = Article.objects.get(pk=id)
            comment.author = request.user
            comment.save()
            print("Комментарий добавлен!")
            return redirect('full-article', id=art.pk)
    else:
        form = AddComment()
    return render(request, 'detail.html', {'art': art, 'form': form, 'comments': comments, 'similar': similar_arts})


class UserProfile(View):
    def get(self, request):
        arts = Article.objects.filter(author=request.user)
        comms = Comment.objects.filter(author=request.user)

        return render(request, 'profile.html', {'arts': arts, 'comms': comms})


class Search(View):
    def get(self, request):
        form = SearchForm()
        arts = []
        return render(request, 'search.html', {'form': form, 'arts': arts})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            arts = Article.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
        else:
            arts = []

        return render(request, 'index.html', {'arts': arts})
