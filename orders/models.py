from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class RegularPizza(models.Model):
    name = models.CharField(max_length=50)
    priceSmall = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.name}, {self.priceSmall}, {self.priceLarge}'


class SicilianPizza(models.Model):
    name = models.CharField(max_length=50)
    priceSmall = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.name}, {self.priceSmall}, {self.priceLarge}'

class PizzaTopping(models.Model):
    topping = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.topping}'


class Sub(models.Model):
    filling = models.CharField(max_length=50)
    priceSmall = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    
    def __str__(self):
        return f'{self.filling}, {self.priceSmall}, {self.priceLarge}'


class Pasta(models.Model):
    filling = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.filling}, {self.price}'


class Salad(models.Model):
    filling = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=4,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.filling}, {self.price}'


class DinnerPlatter(models.Model):
    filling = models.CharField(max_length=50)
    priceSmall = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return f'{self.filling}, {self.priceSmall}, {self.priceLarge}'
