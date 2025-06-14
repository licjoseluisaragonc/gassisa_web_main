from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView, name='index'),
    path('productos/', views.productos, name='productos')
]
