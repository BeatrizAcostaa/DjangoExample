# Generated by Django 5.1.4 on 2024-12-30 20:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chefsTableApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinksCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='drinks',
            name='category_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='chefsTableApp.drinkscategory'),
        ),
    ]
