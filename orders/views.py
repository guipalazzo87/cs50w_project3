from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    pizza = Pizza.objects.all()
    sub = Sub.objects
    pasta = Pasta.objects
    salad = Salad.objects
    dinner = DinnerPlatter.objects

    context = { 
    'pizza': pizza,
    'sub': sub,
    'pasta': pasta,
    'salad': salad,
    'dinner': dinner,
    }
    return render(request, 'orders/index.html', context)