# Generated by Django 3.2.7 on 2021-10-16 21:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations_management', '0046_auto_20211014_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date_location_start',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
