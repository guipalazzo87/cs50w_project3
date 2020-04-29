from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Pizza)
admin.site.register(PizzaTopping)
admin.site.register(Sub)
admin.site.register(SubFilling)
admin.site.register(Pasta)
admin.site.register(PastaFilling)
admin.site.register(Salad)
admin.site.register(SaladFilling)
admin.site.register(DinnerPlatter)
admin.site.register(DinnerFilling)
