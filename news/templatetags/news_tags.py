from django import template

from news.models import *

register = template.Library()


@register.simple_tag()
def getcats():
    return Category.objects.all()


@register.simple_tag()
def total_arts() :
    return Article.objects.count()