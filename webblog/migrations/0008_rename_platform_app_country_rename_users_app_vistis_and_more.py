# Generated by Django 4.0.4 on 2022-06-03 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0007_app_years_alter_app_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='platform',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='app',
            old_name='users',
            new_name='vistis',
        ),
        migrations.RemoveField(
            model_name='app',
            name='years',
        ),
    ]