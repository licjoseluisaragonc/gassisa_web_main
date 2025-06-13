from django.contrib import admin
from django.urls import path
from .views import list_staticfiles

from main.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView, name='index'),
    path('list-staticfiles/', list_staticfiles),
]
