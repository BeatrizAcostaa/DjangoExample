# Generated by Django 5.1.4 on 2024-12-31 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chefsTableApp', '0003_booking'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Drinks',
        ),
        migrations.DeleteModel(
            name='DrinksCategory',
        ),
    ]
