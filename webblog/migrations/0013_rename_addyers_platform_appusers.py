# Generated by Django 4.0.4 on 2022-06-06 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0012_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platform',
            old_name='addYers',
            new_name='appUsers',
        ),
    ]