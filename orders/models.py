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
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Sub(models.Model):
    name = models.CharField(max_length=50)
    priceSmall = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    
    def __str__(self):
        return f'{self.name}, {self.priceSmall}, {self.priceLarge}'


class Pasta(models.Model):
    name = models.CharField(max_length=50)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.name}, {self.priceLarge}'


class Salad(models.Model):
    name = models.CharField(max_length=50)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True)

    def __str__(self):
        return f'{self.name}, {self.priceLarge}'


class DinnerPlatter(models.Model):
    name = models.CharField(max_length=50)
    priceSmall = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)
    priceLarge = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)

    def __str__(self):
        return f'{self.name}, {self.priceSmall}, {self.priceLarge}'
