from django.shortcuts import render
from django.http import HttpResponse

# Vistas de aplicación main index
def IndexView(request):
    ##return HttpResponse("Hola mundo")
    return render(request, "index.html")