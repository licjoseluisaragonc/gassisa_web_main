import os

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

# Vistas de aplicación main index
def IndexView(request):
    return render(request, "index.html")

def productos(request):
    return render(request, 'productos.html')