# Generated by Django 4.1.3 on 2022-11-10 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MenuApp', '0003_rename_category_id_menuitem_category_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='label',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='cuisine',
            old_name='label',
            new_name='title',
        ),
    ]