# Generated by Django 4.0.4 on 2022-06-06 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0013_rename_addyers_platform_appusers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Platform',
        ),
    ]
