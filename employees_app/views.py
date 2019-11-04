from django.shortcuts import render

def show_employees(request):
    return render(request, 'employees.html')
