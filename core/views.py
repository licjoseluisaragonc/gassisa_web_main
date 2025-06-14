import os

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, JsonResponse

# Vistas de aplicación main index
def IndexView(request):
    return render(request, "index.html")

def list_staticfiles(request):
    static_dir = settings.STATIC_ROOT
    files = []
    for root, dirs, filenames in os.walk(static_dir):
        for filename in filenames:
            filepath = os.path.relpath(os.path.join(root, filename), static_dir)
            files.append(filepath)
    return JsonResponse({'static_files': files})

def productos(request):
    return render(request, 'productos.html')