
from statistics import mode
from django.db import models



class app(models.Model):
    visits = models.IntegerField(default=1)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country

class Pie(models.Model):
    value = models.IntegerField(default=1)
    category = models.CharField(max_length=100, default="Catogry")
    
    def __str__(self):
        return self.category

class Chart(models.Model):
    network = models.CharField(max_length=220)
    value = models.IntegerField(default=10)

    def __str__(self):
        return self.network

class Stat(models.Model):
    name = models.CharField(max_length=200)
    value = models.IntegerField(default=15)
    def __str__(self):
        return self.name

class Platform(models.Model):
    appName = models.CharField(max_length=200)
    appUsers = models.IntegerField(default=15)

    def __str__(self):
        return self.appName