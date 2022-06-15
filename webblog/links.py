from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path("charts/", chart),
    path("pie/", piechart),
    path("revir/", revir),
    path('stat/', stat),
    path('platforms/', platform)
]