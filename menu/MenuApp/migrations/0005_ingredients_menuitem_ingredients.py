# Generated by Django 4.1.3 on 2022-11-10 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MenuApp', '0004_rename_label_category_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='menuitem',
            name='ingredients',
            field=models.ManyToManyField(to='MenuApp.ingredients'),
        ),
    ]