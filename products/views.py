from django.shortcuts import render
from products.models import Product, ProductCategory
import os
import json
from datetime import datetime

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
def index(request):
    context = {'title': 'Geekshop',
               'date': datetime.now()}
    return render(request, 'products/index.html', context)


def products(request):
    # file_path_prod = os.path.join(MODULE_DIR, 'fixtures/goods.json') # подгрузка данных из fixtures
    # file_path_cat = os.path.join(MODULE_DIR, 'fixtures/categories.json') # подгрузка данных из fixtures
    context = {'title': 'Geekshop - catalog',
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()
               # 'products': json.load(open(file_path_prod, encoding='utf-8')),  # подгрузка данных из fixtures
               # 'categories': json.load(open(file_path_cat, encoding='utf-8'))  # подгрузка данных из fixtures
               }
    return render(request, 'products/products.html', context)