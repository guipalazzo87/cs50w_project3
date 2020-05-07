from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import *

# Create your views here.

@login_required
def index(request):
    context = {
    'RegularPizza': RegularPizza.objects.order_by('name').all(),
    'SicilianPizza': SicilianPizza.objects.order_by('name').all(),
    'Toppings': PizzaTopping.objects.order_by('name').all(),
    'Sub': Sub.objects.all(),
    'Pasta': Pasta.objects.order_by('name').all(),
    'Salad': Salad.objects.order_by('name').all(),
    'DinnerPlatter': DinnerPlatter.objects.order_by('name').all(),
    }

    return render(request, 'orders/index.html', context)

# def add(request, name, price):
#     item_list = []
#     item_list.append(name)
#     item_list.append(price)
#     print(item_list)
#     return reverse('index')
