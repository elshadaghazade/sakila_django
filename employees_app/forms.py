from django import forms
from .models import Employees

class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'