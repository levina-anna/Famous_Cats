from django.urls import path
from .views import *

urlpatterns = [
    path('', index), # http://127.0.0.1:8000/c
    path('categories/', categories), # http://127.0.0.1:8000/categories/
]