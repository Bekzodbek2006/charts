# Generated by Django 4.0.4 on 2022-06-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0016_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appName', models.CharField(max_length=200)),
                ('appUsers', models.IntegerField(default=15)),
            ],
        ),
    ]
