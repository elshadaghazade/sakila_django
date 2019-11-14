from django.urls import path
from .views import *

urlpatterns = [
    path('', show_employees, name='show_employees'),
    path('reports/', reports, name='reports'),
    path('create/', create_employee, name='create_employee')
]