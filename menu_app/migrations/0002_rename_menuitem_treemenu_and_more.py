# Generated by Django 4.1.7 on 2023-03-08 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MenuItem',
            new_name='TreeMenu',
        ),
        migrations.RenameModel(
            old_name='MenuCategory',
            new_name='TreeMenuCategory',
        ),
    ]
