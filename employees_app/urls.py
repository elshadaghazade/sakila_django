from django.urls import path
from .views import *

urlpatterns = [
    path('', show_employees, name='show_employees')
]