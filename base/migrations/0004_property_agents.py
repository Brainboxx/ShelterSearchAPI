# Generated by Django 4.0 on 2023-08-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_blogcategory_alter_blogpost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='agents',
            field=models.ManyToManyField(related_name='properties', to='base.Agent'),
        ),
    ]
