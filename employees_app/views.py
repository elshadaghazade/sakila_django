from django.shortcuts import render
from .models import Employees
from django.db.models import Q

def show_employees(request):
    search_by_full_name = request.GET.get('full_name')
    search_by_bdate = request.GET.get('b_date')
    search_by_gender = request.GET.get('gender')

    current_page = request.GET.get('page', '')
    try:
        current_page = int(current_page) - 1
    except:
        current_page = 0

    limit = 10
    start = current_page * limit
    
    emps = Employees.objects.all()
    # SELECT * FROM employees

    if search_by_full_name:
        emps = emps.filter(Q(first_name__icontains=search_by_full_name) | Q(last_name__icontains=search_by_full_name))
        # SELECT * FROM employees WHERE first_name like '%asdas%' or last_name like '%asdas%'

    if search_by_bdate:
        emps = emps.filter(Q(birth_date=search_by_bdate))
        # SELECT * FROM employees WHERE (first_name like '%asdas%' or last_name like '%asdas%') and birth_date = '1955-05-25'

    if search_by_gender == "F" or search_by_gender == "M":
        emps = emps.filter(Q(gender=search_by_gender))
        # SELECT * FROM employees WHERE (first_name like '%asdas%' or last_name like '%asdas%') and birth_date = '1955-05-25' and gender = 'F'


    emp_count = emps.count()
    emps = emps[start:start+limit]
    page_numbers = (emp_count // limit) + 1

    return render(request, 'employees.html', context={
        'employees': emps,
        'page_numbers': range(1, page_numbers+1)
    })
