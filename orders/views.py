from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    pizza = Pizza.objects.all()
    sub = Sub.objects.all()
    pasta = Pasta.objects.all()
    salad = Salad.objects.all()
    dinner = DinnerPlatter.objects.all()

    context = { 
    'pizza': pizza,
    'sub': sub,
    'pasta': pasta,
    'salad': salad,
    'dinner': dinner,
    }
    return render(request, 'orders/index.html', context)