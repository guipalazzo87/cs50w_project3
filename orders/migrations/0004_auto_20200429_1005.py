# Generated by Django 3.0.5 on 2020-04-29 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200429_1004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
