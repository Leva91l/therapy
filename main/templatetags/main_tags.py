from django import template

from main.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

@register.simple_tag()
def get_products(filter=None):
    if not filter:
        return Product.objects.all()
    else:
        return Product.objects.filter(cat_id=filter)
