# Generated by Django 3.0.5 on 2020-04-29 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_toppings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='toppings',
            new_name='number_toppings',
        ),
    ]
