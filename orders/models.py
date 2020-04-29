from django.db import models

# Create your models here.



class PizzaTopping(models.Model):
    topping = models.CharField(max_length=50)

    def __str__(self):
        return self.topping

class Pizza(models.Model):
    large = models.BooleanField(default=None)
    number_toppings = models.IntegerField(default=0)
    toppings = models.ManyToManyField(PizzaTopping, blank=True)
    sicilian = models.BooleanField(default=None)

#    def __str__(self):
#        return self.toppings



class SubFilling(models.Model):
    filling = models.CharField(max_length=50)
    priceSmall = models.FloatField()
    priceLarge = models.FloatField()

    def __str__(self):
        return self.filling


class Sub(models.Model):
    large = models.BooleanField(default=None)
    filling = models.ManyToManyField(SubFilling, blank=True)
    xtra_cheese = models.BooleanField(default=None)

    def __str__(self):
        return self.filling

class PastaFilling(models.Model):
    filling = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.filling

class Pasta(models.Model):
    filling = models.ManyToManyField(PastaFilling, blank=True)

    def __str__(self):
        return self.filling

class SaladFilling(models.Model):
    filling = models.CharField(max_length=50)
    price = models.FloatField()

    def __str__(self):
        return self.filling

class Salad(models.Model):
    filling = models.ManyToManyField(SaladFilling, blank=True)

    def __str__(self):
        return self.filling

class DinnerFilling(models.Model):
    filling = models.CharField(max_length=50)
    priceSmall = models.FloatField()
    priceLarge = models.FloatField()

    def __str__(self):
        return self.filling

class DinnerPlatter(models.Model):
    large = models.BooleanField(default=None)
    filling = models.ManyToManyField(DinnerFilling, blank=True)

    def __str__(self):
        return self.filling