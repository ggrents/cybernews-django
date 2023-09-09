from django.http import Http404
from django.shortcuts import render
from news.models import *


def show_article(request):
    arts = Article.objects.all()
    cats = Category.objects.all()
    return render(request, 'index.html', {'articles': arts, 'cats' : cats})

def show_recent_article(request) :
    arts = Article.objects.order_by('-created')[:3]
    cats = Category.objects.all()
    return render(request, 'index.html', {'articles': arts, 'cats':cats})

def show_only_category(request, slug) :
    chosen_category = Category.objects.get(slug=slug)
    arts = Article.objects.filter(category=chosen_category)
    return render(request, 'dotacat.html', {'articles': arts} )

def article_detail(request, id):
    try:
        art = Article.objects.get(pk=id)
        print(art)
    except Article.DoesNotExist:
        raise Http404("No article found with that id")
    return render(request, 'detail.html', {'art': art})
