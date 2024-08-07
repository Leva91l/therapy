from django.shortcuts import render

from main.models import Category, Product
from .forms import CoopRequest

# Create your views here.
#
# def add_new_product(request):
menu = [
    {'title': 'Контакты', 'url_link': 'contacts'},
    {'title': 'На главную', 'url_link': 'homepage'},
    {'title': 'Для сотрудничества', 'url_link': 'coop'},

]


def homepage(request):
    product = Product.objects.all()

    context = {
        'menu': menu,
        'product': product
    }
    return render(request, 'homepage.html', context)


def prodview(request, prod_slug):
    category = Category.objects.filter(slug=prod_slug)
    product = Product.objects.filter(cat_id=category[0])
    context = {
        'menu': menu,
        'product': product,
        'category': category
    }
    return render(request, 'products.html', context)


def contacts(request):
    return render(request, 'contacts.html')


def productinfo(request, product_slug):
    product = Product.objects.filter(slug=product_slug)
    context = {
        'product': product,
        'menu': menu
    }
    return render(request, 'productinfo.html', context)


def coop(request):#функция для запроса на сотрудничество
    # должна передавать запрос от клиента из формы на сотрудничество куда нибудь
    dict_req = {}
    if request.method == 'POST':
        cooperation = CoopRequest(request.POST)
        if cooperation.is_valid():
            dict_req = cooperation.cleaned_data
    else:
        cooperation = CoopRequest()
    context = {
        'coop': cooperation
    }
    print('11')
    print(dict_req)
    return render(request, 'coop.html', context)
