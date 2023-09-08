from django.http import Http404
from django.shortcuts import render
from news.models import Article


def show_article(request):
    arts = Article.objects.all()
    return render(request, 'index.html', {'articles': arts})

def show_recent_article(request) :
    arts = Article.objects.order_by('-created')[:3]
    return render(request, 'index.html', {'articles': arts})

def article_detail(request, id):
    try:
        art = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        raise Http404("No article found with that id")
    return render(request, 'detail.html', {'art': art})
