# Generated by Django 4.0.4 on 2022-06-03 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webblog', '0005_fourth'),
    ]

    operations = [
        migrations.CreateModel(
            name='app',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.IntegerField(max_length=4294967295)),
                ('platform', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='First',
        ),
        migrations.DeleteModel(
            name='Fourth',
        ),
        migrations.DeleteModel(
            name='Second',
        ),
        migrations.DeleteModel(
            name='Third',
        ),
    ]