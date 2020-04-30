from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import *

# Create your views here.

@login_required
def index(request):
    varRegularPizza = RegularPizza.objects.all(),
    varSicilianPizza = SicilianPizza.objects.all(),
    varPizzaTopping = PizzaTopping.objects.all(),
    varSub = Sub.objects.all(),
    varPasta = Pasta.objects.all(),
    varSalad = Salad.objects.all(),
    varDinnerPlatter = DinnerPlatter.objects.all(),

    context = {
    'RegularPizza': varRegularPizza,
    'SicilianPizza': varSicilianPizza,
    'Toppings': varPizzaTopping,
    'Sub': varSub,
    'Pasta': varPasta,
    'Salad': varSalad,
    'DinnerPlatter': varDinnerPlatter,
    }
    return render(request, 'orders/index.html', context)



'''
This functions seens to reach from the database, querying for 
some input from the user, I'm not sure how, and return two itens:
menu (with the options selected by the category) and how many
columns are there. The columns will be used in index.html to determine
what layout will be shown to the client

The category is passed from URL in 
'''

def findTable(category):
    if category == "Regular Pizza":
        menu=Regular_pizza.objects.all()
        columns=3
    elif category == "Sicilian Pizza":
        menu=Sicilian_pizza.objects.all()
        columns=3
    elif category == "Toppings":
        menu=Topping.objects.all()
        columns=1
    elif category == "Subs":
        menu=Sub.objects.all()
        columns=3
    elif category == "Pasta":
        menu=Pasta.objects.all()
        columns=2
    elif category == "Salad":
        menu=Salad.objects.all()
        columns=2
    elif category == "Dinner Platters":
        menu=Dinner_platter.objects.all()
        columns=3

    return menu,columns
