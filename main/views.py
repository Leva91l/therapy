from django.http import HttpResponse
from django.shortcuts import render

from main.models import Category, Product

# Create your views here.
#
# def add_new_product(request):
menu = [
    {'title': 'Контакты', 'url_link': 'contacts'}
]


# формирование ссылки - в шаблоне страницы из которой нужен переход формируем ссылку(если нужен параметр то прописыва5ем его через пробел

def homepage(request):
    category = Category.objects.all()
    product = Product.objects.all()

    context = {
        'cats': category,
        'menu': menu,
        'product': product
    }
    return render(request, 'homepage.html', context)


def new_product(request):
    product = Product(
        name='Простыни одноразовые в рулоне 80 мкр',
        content='ть 15 гр.',
        cat_id=2
    )
    product.save()
    return HttpResponse('Success!')


def prodview(request, prod_id):
    product = Product.objects.filter(cat_id=prod_id)
    category = Category.objects.filter(id=prod_id)
    context = {
        'menu': menu,
        'product': product,
        'category': category
    }
    return render(request, 'products.html', context)


# сформировать категории на главной странице(написать view функцию, либо передать в контекст )
def contacts(reqest):
    return render(reqest, 'contacts.html')
