# Generated by Django 3.0.5 on 2020-04-29 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200429_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saladfilling',
            old_name='priceLarge',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='saladfilling',
            name='priceSmall',
        ),
    ]
