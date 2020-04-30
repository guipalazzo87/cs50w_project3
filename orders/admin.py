from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(RegularPizza)
admin.site.register(SicilianPizza)
admin.site.register(PizzaTopping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
