# Generated by Django 4.1.3 on 2022-11-10 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuApp', '0005_ingredients_menuitem_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]