from django.contrib import admin
from .models import *

admin.site.register(Departments)
admin.site.register(DeptManager)
admin.site.register(DeptEmp)