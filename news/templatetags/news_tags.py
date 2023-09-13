from django import template

from news.models import *

register = template.Library()


@register.simple_tag()
def getcats():
    return Category.objects.all()


