from multiprocessing import context
from django.shortcuts import render
from .models import *
def home(request):
    return render(request, 'index.html')
def chart(request):
    fun = app.objects.all()
    context = {
        "chart": fun
    }
    return render(request, 'charts.html', context)
def piechart(request):
    fun = Pie.objects.all()
    context = {
        "pie": fun
    }
    return render(request, 'pie.html', context)

def revir(request):
    fun  = Chart.objects.all()
    context = {
        "charts": fun
    }
    return render(request, 'anchor.html', context)

def stat(request):
    fun = Stat.objects.all()
    context = {
        "chart":fun
    }
    return render(request, 'statistika.html', context)

def platform(request):
    fun = Platform.objects.all()

    context = {
        "base": fun
    }
    return render(request, 'platform.html', context)