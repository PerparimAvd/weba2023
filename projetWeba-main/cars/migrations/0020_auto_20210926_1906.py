# Generated by Django 3.2.7 on 2021-09-26 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0019_auto_20210926_1903'),
    ]

    operations = [
        migrations.RenameField(
            model_name='illimited_kms',
            old_name='illimited_kms',
            new_name='illimited_kms_price',
        ),
        migrations.RenameField(
            model_name='price_category',
            old_name='price_category',
            new_name='unlimited_kms_price',
        ),
    ]
