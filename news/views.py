from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
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
        form = AddArticle(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Статья Добавлена!")
    else:
        form = AddArticle()

    return render(request, 'addart.html', {'form': form})


def show_recent_article(request):
    arts = Article.objects.order_by('-created')[:3]
    cats = Category.objects.all()
    return render(request, 'index.html', {'arts': arts, 'cats': cats})


def show_only_category(request, slug):
    chosen_category = Category.objects.get(slug=slug)
    arts = Article.objects.filter(category=chosen_category)
    return render(request, 'dotacat.html', {'articles': arts})


def article_detail(request, id):
    try:
        art = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        raise Http404("No article found with that id")
    return render(request, 'detail.html', {'art': art})
