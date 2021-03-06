# Generated by Django 3.0.5 on 2020-04-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200429_1029'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubFilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filling', models.CharField(max_length=50)),
                ('priceSmall', models.FloatField()),
                ('priceLarge', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='sub',
            name='filling',
        ),
        migrations.AddField(
            model_name='sub',
            name='filling',
            field=models.ManyToManyField(blank=True, to='orders.SubFilling'),
        ),
    ]
