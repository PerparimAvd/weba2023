# Generated by Django 3.2.7 on 2021-09-27 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0022_price_category_illimited_kms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_category',
            name='illimited_kms',
        ),
    ]
