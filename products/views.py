from django.shortcuts import render
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
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {'title': 'Geekshop - catalog',
               'products': json.load(open(file_path, encoding='utf-8'))}
    return render(request, 'products/products.html', context)