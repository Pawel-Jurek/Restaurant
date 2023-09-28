# Generated by Django 4.2.2 on 2023-09-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_dish_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.CharField(choices=[('breakfast', 'śniadanie'), ('main_course', 'danie_główne'), ('dessert', 'deser'), ('drink', 'napój')], max_length=15),
        ),
    ]
